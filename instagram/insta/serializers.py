from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login
from rest_framework import exceptions
from django.db.models import Q
from rest_framework.serializers import(ModelSerializer,EmailField,IntegerField)
from django.contrib.auth import get_user_model
from rest_framework import request
from rest_framework.serializers import ValidationError

#from .models import (Post,Activity,Comment,Friend)
from .models import *
from django.contrib.auth import get_user_model
User=get_user_model()

class LoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField(style={'input_type': 'password'},required=True)
    print("1")

    class Meta:
        print("6")
        model = User
        fields = ['username','password',]
        extra_kwargs = {"password": {"write_only": True}
                       }

    def validate(self,data):
        username=data['username']
        password=data['password']
        print("2")


        if username and password:
            print("3")
            user=authenticate(username=username,password=password)
            if user:
                if user.is_active:
                    data["user"]=user
                else:
                    msg="User is deactivated"
                    raise exceptions.ValidationError(msg)
            else:
                print("4")
                msg="Unable to login with given credentials"
                raise exceptions.ValidationError(msg)
        else:
            msg="Must provide username and password both"
            raise exceptions.ValidationError(msg)


        return data

User=get_user_model()
class UserCreateSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(label='Email Address')
    password = serializers.CharField(style={'input_type': 'password'},required=True)
    username=serializers.CharField()
    first_name=serializers.CharField()
    last_name=serializers.CharField()

    class Meta:
        model = User
        write_only_fields = ('password',)
        read_only_fields = ['id']
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name']

        extra_kwargs = {
            "password": {"write_only": True},
        }

    def validate(self, data):
         k=0
         email=data['email']
         username=data['username']
         password=data['password']
         validLetters = "abcdefghijklmnopqrstuvwxyz"

         query=User.objects.filter(username=username)
         for char in username.lower():
             if (char in validLetters):
                 k=1
         if (k==0):
             raise ValidationError("Must contain alphabets")


         if (len(username)<=4):
             raise ValidationError("Username is too short")
         if (len(password)<=4):
             raise ValidationError("password is too short")
         if query.exists():
             raise ValidationError("User with this name already exists!!")
         user_qs=User.objects.filter(email=email)
         if user_qs.exists():
              raise ValidationError("This email has already been registered!!")
         return data


    def create(self, validated_data):
      user = User.objects.create(
          username=validated_data['username'],
          email=validated_data['email'],
          first_name=validated_data['first_name'],
          last_name=validated_data['last_name'],
          password=validated_data['password'],
      )
      user.set_password(validated_data['password'])
      user.is_active=False
      user.save()
      return user

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id','image','bio','phone_no','username')
        read_only_fields = ('id','username')

class PostSerializer(serializers.ModelSerializer):
     p = serializers.SerializerMethodField()
     like =serializers.SerializerMethodField()
     class Meta:
        model = Post
        fields = ('id','title','caption','picture','files','date_created','name','user','p','like')
        read_only_fields = ('id','name','user','p','like')

     def get_p(self, obj):
         k=User.objects.get(id=obj.user.id)
         print(k)
         seria=ProfileSerializer(k)
         return (seria.data)
     def get_like(self,obj):
         post = Post.objects.get(id=obj.id)
         result= Activity.objects.filter(post=post).count()
         return (result)

class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Activity
        fields = ('user', 'post', 'like')
        read_only_fields = ('user', 'post')


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id','user','post','text','name')
        read_only_fields = ('user','post','id','name')

class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = ('user','current_user')
        read_only_fields = ('current_user','user')

class OtpSerializer(serializers.ModelSerializer):

    class Meta:
        model= otp_generate
        fields = ('user','otp','otp_sent')
        read_only_fields= ['user']
class PasswordEmail(serializers.Serializer):
    email_field=serializers.EmailField(required=True)
    class Meta:
        field='email_field'
class ChangePassword(serializers.Serializer):
    new_password=serializers.CharField(style={'input_type': 'password'},required=True)
    confirm_password=serializers.CharField(style={'input_type': 'password'},required=True)
    otp = serializers.IntegerField(default=0)
    class Meta:
        field=('otp','new_password','otp')

class RequestSerializer(serializers.ModelSerializer):
    p=serializers.SerializerMethodField()
    q = serializers.SerializerMethodField()
    class Meta:
        model =FriendRequest
        fields =('id','p','q','timestamp')
        read_only_fields=('id','p','q','timestamp')

    def get_p(self, obj):
        k = User.objects.get(id=obj.to_user.id)
        print(k)
        seria = ProfileSerializer(k)
        return (seria.data)
    def get_q(self, obj):
        k = User.objects.get(id=obj.from_user.id)
        print(k)
        seria = ProfileSerializer(k)
        return (seria.data)
