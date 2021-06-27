from typing import TYPE_CHECKING
from django.shortcuts import render, redirect
import bcrypt, re, requests
from django.contrib import messages
from .models import *


def splash(request):
    return render(request, 'splash.html')

def loginreg(request):
    return render(request, 'loginreg.html')

def infopage(request):
    return render(request, 'infopage.html')

def profile(request):
    return render(request, 'profile.html')
