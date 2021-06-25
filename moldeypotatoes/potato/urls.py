from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    path('', views.splash, name='splash'),
    path('loginreg', views.login, name='loginreg'),
]