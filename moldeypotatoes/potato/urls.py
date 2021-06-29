from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    path('', views.splash, name='splash'),
    path('loginreg', views.loginreg, name='loginreg'),
    path('infopage', views.infopage, name='infopage'),
    path('profile', views.profile, name='profile'),
    path('create_user', views.create_user, name='create_user')
]
