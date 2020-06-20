from django.db import models
#from __future__import unicode_literals

# Create your models here.
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
# from django.contrib.auth.models import User
# from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# class Profile(models.Model):
#     #owner = models.ForeignKey('auth.User', related_name='profiles', on_delete=models.CASCADE)
#     user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
#     name = models.CharField(max_length=250,blank=True)
#     image=models.ImageField(upload_to='profile_images',blank=True)
#     bio = models.TextField(max_length=500, blank=True)
#     phone_no =PhoneNumberField()
#     #birth_date = models.DateField(null=True,blank=True)
#     def __str__(self):
#         return self.user.username
#
#
#     @receiver(post_save, sender=User)
#     def create_profile(sender, instance, created, **kwargs):
#         if created:
#             Profile.objectscreate(user=instance)
#
#     @receiver(post_save, sender=User)
#     def save_profile(sender, instance, **kwargs):
#         instance.profile.save()

class User(AbstractUser):
    #user = models.OneToOneField(settings.AUTH_USER_MODEL)
    #name = models.CharField(max_length=250, blank=True)
    image=models.ImageField(upload_to='profile_images',blank=True)
    bio = models.TextField(max_length=500, blank=True)
    phone_no = PhoneNumberField(blank=True)
    def __str__(self):
        return self.username

class Post(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=250,blank=True)
    title = models.CharField(max_length=255,null=True,blank=True)
    caption=models.TextField(max_length=500, blank=True,null=True)
    picture=models.ImageField(upload_to='images',blank=True)
    files=models.FileField(upload_to='file',blank=True)
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s"%(self.caption)

    class Meta:
        ordering = ['-date_created']

class Activity(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    like_count = models.PositiveIntegerField(default=0)
    def __str__(self):
        return (self.post.id)


class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    text = models.TextField(max_length=500, blank=True,null=True)
    name = models.CharField(max_length=250,blank=True)

    def __str__(self):
        return("%s post.id %s"%(self.post.id,self.text))

    #created_date = models.DateTimeField(auto_now_add=True)


class Friend(models.Model):
    user = models.ManyToManyField(User)
    current_user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='current',
                                     null=True)
    # @classmethod
    # def make_friend(cls,current_user,new_friend):
    #     print('hello')
    #     if (new_friend !=current_user):
    #         print("54")
    #         friend,created = cls.objects.get_or_create(current_user=current_user)
    #         friend.user.add(new_friend)
    #         print("hello")
    #         print(friend.user.all())
    #
    # @classmethod
    # def lose_friend(cls,current_user,new_friend):
    #     if (new_friend !=current_user):
    #         friend,created = cls.objects.get_or_create(current_user=current_user)
    #         friend.user.remove(new_friend)
    #         print(friend.user.all())

    def __str__(self):
        return("%s"%(self.current_user))

class otp_generate(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    otp=models.PositiveIntegerField(default=0)
    otp_sent = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return ("%s"%(self.otp))

class FriendRequest(models.Model):
    to_user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='to_user')
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='from_user')
    timestamp=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "From {},to {}".format(self.to_user.username,self.from_user.username)




