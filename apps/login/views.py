# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Users
import bcrypt
import re

ereg = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your views here.
def index(request):
    print Users.objects.all()
    return render(request, 'index.html')

def reg(request):
    success = True
    fname = request.POST['fname']
    lname = request.POST['lname']
    remail = request.POST['email']
    passw = request.POST['pass']
    cpass = request.POST['cpass']
    hashpass = bcrypt.hashpw(passw.encode(), bcrypt.gensalt())
    if len(fname) < 2:
        messages.add_message(request, messages.INFO, 'First name must be more than 2 characters.')
        success = False
    if fname.isalpha() != True:
        messages.add_message(request, messages.INFO,'First name must be alphabetical charaters only.')
        success = False
    if len(lname) < 2:
        messages.add_message(request, messages.INFO,'Last name must be more than 2 characters.')
        success = False
    if lname.isalpha() != True:
        messages.add_message(request, messages.INFO,'Last name must be alphabetical charaters only.')
        success = False
    if not ereg.match(remail):
        messages.add_message(request, messages.INFO,'Must enter a valid email.')
        success = False
    if len(passw) < 8:
        messages.add_message(request, messages.INFO,'Password must be more than 8 characters.')
        success = False
    if passw != cpass:
        messages.add_message(request, messages.INFO,'Password and confirm password must match.')
        success = False
    if success == False:
        return redirect('/')
        
    Users.objects.create(first_name=fname, last_name=lname, email=remail, password=hashpass)
    return redirect('/regsuccess')

def login(request):
    remail = request.POST['email']
    passw = request.POST['pass']
    hashpass = bcrypt.hashpw(passw.encode(), bcrypt.gensalt())
    x = Users.objects.filter(email = remail)
    y = Users.objects.filter(password=hashpass)
    print hashpass
    print x
    print y
    if len(x) > 1 and len(y) > 1:
        return redirect('/loginsuccess')
    else:
        messages.add_message(request, messages.INFO, "Incorrect email or password")
        return redirect('/')

def regsuccess(request):
    messages.add_message(request, messages.INFO, "Registration Successful!")
    return render(request, 'regsuccess.html')

def loginsuccess(request):
    messages.add_message(request, messages.INFO,"Login Successful!")
    return render(request, 'loginsuccess.html') 