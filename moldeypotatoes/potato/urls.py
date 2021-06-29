from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    path('', views.splash, name='splash'),
    path('loginreg', views.loginreg, name='loginreg'),
    path('infopage/<int:id>', views.infopage, name='infopage'),
    path('profile', views.profile, name='profile'),
    path('create_user', views.create_user, name='create_user'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('games', views.games, name='games'), 
    path('books', views.games, name='games'),
    path('movies', views.games, name='games'),
]
