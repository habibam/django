# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from models import User

# Create your views here.
def test(request):
    return HttpResponse('Sucess!')

def main(request):
    return render(request, 'LoginRegistration_app/index.html')


def register(request):
    errors = User.objects.validate(request.POST)

    if len(errors) > 0:
        context = {
            'errors': errors,
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'email': request.POST['email'],
            'birthday': request.POST['birthday'],
        }
        return render(request, 'LoginRegistration_app/index.html', context)

    else:
        newUser = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'],
            password=request.POST['password'], birthday=request.POST['birthday'])
        return redirect('/success/{}'.format(newUser.id))


def success(request, userID):
    context = {
        'name': User.objects.get(id=userID).first_name,
    }
    return render(request, 'LoginRegistration_app/success.html', context)


def login(request):
    errors = User.objects.validate_login(request.POST)
    if len(errors) > 0:
        context = {
            'errors': errors,
        }
        return render(request, 'LoginRegistration_app/index.html', context)
    else:
        context = {
            'name': User.objects.get(email=request.POST['login_email']).first_name,
        }
    return render(request, 'LoginRegistration_app/success.html', context)