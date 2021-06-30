from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', views.splash, name='splash'),
    path('loginreg', views.loginreg, name='loginreg'),
    path('infopage/', views.infopage, name='infopage'),
    path('profile', views.profile, name='profile'),
    path('create_user', views.create_user, name='create_user'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('all_games', views.all_games, name='games'), 
    path('all_books', views.all_books, name='games'),
    path('all_movies', views.all_movies, name='games'),

    path('book_info', views.book_info, name='book_info'),
    path('game_info', views.game_info, name='game_info'),
    path('movie_info', views.movie_info, name='movie_info'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

