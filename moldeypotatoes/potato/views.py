from django.shortcuts import render, redirect
from .models import User, Book, Movie, Game, Review
from django.contrib import messages
import bcrypt

def loginreg(request):
    return render(request, 'loginreg.html')

def infopage(request):
    return render(request, 'infopage.html')

def profile(request):
    return render(request, 'profile.html')

def splash(request):
    return render(request, 'splash.html')

def create_user(request):
    if request.method == 'POST':
        errors = {}
        errors = User.objects.register_validation(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request,value)
                return redirect('/login')
        hash_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        new_user = User.objects.create(
            user_name= request.POST['user_name'],
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            password = hash_pw,
        )
        request.session['logged_user'] = new_user.id
        return redirect('splash.html')
    return redirect('/login')

def login(request):
    if request.method == 'POST':
        errors = {}
        errors = User.objects.login_validation(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
                return redirect('/login')
        user = User.objects.filter(email = request.POST['email'])
        if user:
            logged_user = user[0]
            if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                request.session['logged_user'] = logged_user.id
    return redirect('profile.html')

def logout(request):
    request.session.flush()
    return redirect('placeholder.html')

