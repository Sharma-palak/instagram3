from django.contrib.auth import get_user_model
User=get_user_model()
from rest_framework import permissions
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        # print('00')
        # print(obj.user.id)
        # print(request.user.id)
        return obj.id == request.user.id

class IsPostOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        print(obj.user.id)
        print(request.user.id)
        return obj.user.id == request.user.id


class IsCommentOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        print(obj.user.id)
        print(request.user.id)
        return obj.user.id == request.user.id