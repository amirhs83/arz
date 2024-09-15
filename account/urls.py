from django.urls import path
from .views import LoginView,SignUpUser,LogoutUser,VerifyCode,VerifyCode2,LoginUser,Card


app_name='account'

urlpatterns=[
    path('loginview/',LoginView.as_view(),name='loginview'),
   
    path('signup/',SignUpUser.as_view(),name='signupuser'),

    path('logout/',LogoutUser.as_view(),name='logout'),
     path('verify/',VerifyCode.as_view(),name='verify'),
    path('verify2/',VerifyCode2.as_view(),name='verify2'),

       path('loginuser/',LoginUser.as_view(),name='loginuser'),
       
       path('card/',Card.as_view(),name='card'),

] 