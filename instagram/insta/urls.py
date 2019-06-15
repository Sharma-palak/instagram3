from django.conf.urls import url
from django.urls import path,include
from .import views
from django.conf import settings
from rest_framework_jwt.views import obtain_jwt_token

from django.conf.urls import url
from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'post', views.PostView)
router.register(r'profile',views.ProfileView)
router.register(r'comment_edit',views.Comment_Edit)
router.register(r'add_friend',views.Add_Friend,basename='add_friend')
router.register(r'delete',views.DeleteAccount)
router.register(r'request',views.Request)

urlpatterns = [
    path('',include(router.urls)),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view()),
    url(r'^like/(?P<postid>[0-9]+)/$',LikeView.as_view()),
    url(r'^comment/(?P<postid>[0-9]+)/$',CommentView.as_view()),
    #url('^add_friend/(?P<operation>[0-9]+)/$',Add_Friend.as_view()),
    url(r'^register/$', UserCreateAPIView.as_view(),name='register'),
    #url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #Activate.as_view(), name='activate'),
    url('^friend_list/(?P<userid>[0-9]+)/$',Friend_List.as_view()),
    url('^otp_activate/(?P<id>[0-9]+)/$',otp_verify.as_view()),
]
