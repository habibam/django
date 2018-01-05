# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import Pet

# Create your views here.

def createPet(request):
    results = Pet.objects.validatePet(request.POST)
    if results['status']:
        newPet = Pet.objects.createPet(request.POST)
    else:
        return redirect('/user/show/{}'.format(request.session['currentUser']))

def deletePet(request, petID):
    Pet.objects.get(id=petID).delete()
    return redirect('/user/show/{}'.format(request.session['currentUser']))
