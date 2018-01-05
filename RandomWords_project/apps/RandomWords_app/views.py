# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string


# Create your views here.
def index(request):
    if not 'attempt' in request.session:
        request.session['attempt'] = 0
        request.session['random_word'] ='No Random Word Yet'
    return render(request, 'RandomWords_app/index.html')

def generate(request):
    request.session['attempt'] +=1
    request.session['random_word'] = get_random_string(14)
    return redirect('/')

def reset(request):
    request.session.pop('attempt')
    request.session.pop('random_word')
    return redirect('/')