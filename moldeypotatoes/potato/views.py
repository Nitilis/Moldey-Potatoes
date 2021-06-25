from typing import TYPE_CHECKING
from django.shortcuts import render, redirect
import bcrypt, re, requests
from django.contrib import messages
from .models import *


def splash(request):
    return render(request, 'splash.html')
