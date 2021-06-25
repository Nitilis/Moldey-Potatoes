from django.db import models
import re

from django.db.models.base import Model
import bcrypt

class UserManager(models.Manager):
    def register_validation(self,form):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        used_email = User.objects.filter(email = form['email'])
        if len(form['first_name']) < 1:
            errors['first_name'] = 'Invalid First Name'
        if len(form['last_name']) < 1:
            errors['last_name'] = 'Invalid Last Name'
        if not EMAIL_REGEX.match(form['email']):
            errors['email'] = 'Invalid Email'
        elif used_email:
            errors['used'] = 'Email already in use'
        if len(form['password']) < 6:
            errors['password'] = 'Password should be 6 characters long'
        elif form['password'] != form['confirmpw']:
            errors['confirmpw'] = 'Passwords do not match'
        return errors
    
    def login_validation(self,form):
        errors = {}
        email = User.objects.filter(email = form['email'])
        if not email or not bcrypt.checkpw(form['password'].encode(), email[0].password.encode()):
            errors['wrong'] = 'Email or Password is wrong'
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    publisher = models.CharField(max_length=50)
    genre = models.CharField(max_length=20)
    release_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Movie(models.Model):
    title = models.CharField(max_length=50)
    director = models.CharField(max_length=50)
    genre = models.CharField(max_length=20)
    trailer_link = models.URLField()
    release_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Game(models.Model):
    title = models.CharField(max_length=50)
    creator = models.CharField(max_length=50)
    genre = models.CharField(max_length=20)
    trailer_link = models.URLField()
    release_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

#class Review(models.Model):
    
