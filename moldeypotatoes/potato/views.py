from django.shortcuts import render, redirect
from .models import User, Book, Movie, Game, Review
from django.contrib import messages
import bcrypt

def loginreg(request):
    return render(request, 'loginreg.html')

def profile(request):
    if "user_id" not in request.session:
        return redirect('/')

    context= {
        'user' : User.objects.get(id=request.session['user_id']),
    }
    return render(request, 'profile.html', context)


def splash(request):
    if 'user_id' in request.session:
        user_logged_in = True
    else:
        user_logged_in = False
    context = {
        'logged_in' : user_logged_in
    }
    return render(request, 'splash.html',context)

def create_user(request):
    if request.method == 'POST':
        errors = User.objects.register_validation(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request,value)
            return redirect('/loginreg')
        else:
            hash_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
            new_user = User.objects.create(
                user_name= request.POST['user_name'],
                first_name = request.POST['first_name'],
                last_name = request.POST['last_name'],
                email = request.POST['email'],
                password = hash_pw)
            request.session['logged_user'] = new_user.id
            return redirect('/profile')
    return redirect('/loginreg')

def login(request):
    if request.method == 'POST':
        errors = User.objects.login_validation(request.POST)
        if errors:
            for key, value in errors.items():
                messages.error(request,value)
            return redirect('/loginreg')
        else:
            logged_user = User.objects.filter(email = request.POST['email'])
            request.session['user_id'] = logged_user[0].id
            return redirect('profile.html')
    else:
        return redirect('/loginreg')

def logout(request):
    request.session.flush()
    return redirect('placeholder.html')

def all_games(request):
    context = {
        'all_games': Game.objects.all(),
    }
    return render(request, 'games.html', context)

def all_books(request):
    context = {
        'all_books': Book.objects.all(),
    }
    return render(request, 'books.html', context)

def all_movies(request):
    context = {
        'all_movies': Movie.objects.all(),
    }
    return render(request, 'movies.html', context)

def movie_info(request, movie_id):
    if "user_id" not in request.session:
        return redirect('/')
    context = {
        'movie' : Movie.objects.get(id=movie_id),
    }
    return render(request, 'movieinfo.html', context)

def game_info(request, game_id):

    if "user_id" not in request.session:
        return redirect('/')

    context = {
        'game': Game.objects.get(id=game_id),
    }
    return render(request, 'gameinfo.html', context)


def book_info(request, book_id):

    if "user_id" not in request.session:
        return redirect('/')

    # if "user_id" not in request.session:
    #     return redirect('/')

    context = {
        'book': Book.objects.get(id=book_id),
    }
    return render(request, 'bookinfo.html', context)
