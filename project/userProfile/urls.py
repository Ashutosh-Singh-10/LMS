from django.contrib import admin
from django.urls import path,include
from .views import * 


urlpatterns = [
    path('',ProfileView.as_view()),
    path('updateavatar',UpdateAvatar.as_view()),
    path('update',UpdateProfile.as_view()),


]
