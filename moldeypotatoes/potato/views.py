from django.shortcuts import render, redirect
from .models import User, Book, Movie, Game
from django.contrib import messages
import bcrypt

# Create your views here.
def index(request): #?
return render (request, 'placeholder.html')

def create_user(request):
    if request.method == 'POST':
        errors = {}
        errors = User.objects.register_validation(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request,value)
                return redirect('/login')
        hash_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        new_user = Users.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            password = hash_pw,
        )
        request.session['logged_user'] = new_user.id
        return redirect('/profile')#REDIRECT TO PROFILE OR PLACEHOLDER?
    return redirect('/login')
    
def login(request):
    if request.method == 'POST':
        errors = {}
        errors = login_validation(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
                return redirect('/login')
        user = User.objects.filter(email = request.POST['email'])
        if user:
            logged_user = user[0]
            if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                request.session['logged_user'] = logged_user.id
    return redirect('placeholder.html')
  
  
  
  
  
  def logout(request):
    request.session.flush()
    return redirect('placeholder.html')
