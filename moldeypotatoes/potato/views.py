from django.shortcuts import render, redirect
from .models import User, Book, Movie, Game, Review
from django.contrib import messages
import bcrypt

def loginreg(request):
    return render(request, 'loginreg.html')

def infopage(request):
    if "user_id" not in request.session:
        return redirect('/')
    return render(request, 'infopage.html')

def profile(request):
    if "user_id" not in request.session:
        return redirect('/')
    return render(request, 'profile.html')

def splash(request):
    return render(request, 'splash.html')

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
            return redirect('/')
    else:
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
            return redirect('/')
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
