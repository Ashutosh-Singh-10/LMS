from django.contrib import admin
from django.urls import path,include
from .views import * 
from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('refresh',TokenRefreshView.as_view()),
    path('',TokenObtainPairView.as_view(),name="TokenObtainPairView"),
    path('createuser',CreateUser.as_view()),
    path('otp',OTPView.as_view()),
    path('delete',DeleteUserView.as_view()),

]