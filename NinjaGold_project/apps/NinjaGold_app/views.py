# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
import random


# Create your views here.
def main(request):
    try:
        request.session['gold']
    except KeyError:
        request.session['gold'] = 0

    try:
        request.session['activity']
    except KeyError:
        request.session['activity'] = []

    context={
        'gold': request.session['gold'],
    }
    return render(request, 'NinjaGold_app/index.html', context)

def process_money(request, building):
    #rolls for random amount depending on which building
    print request.session['activity']
    thisActivity = {}
    randGold = 0

    if building == "Farm":
        randGold = random.randint(10, 20)
    elif building == "Cave":
        randGold = random.randint(5, 10)
    elif building == "House":
        randGold = random.randint(2, 5)
    elif building == "Casino":
        randGold = random.randint(0,100)-50

    else:#impossible unless the user meddles with dev tools
        thisActivity['loss'] = "You get sucked into a black hole!!"

    #populates activity string and modifies gold value based on above
    if request.session['gold'] == 0 and building == "Casino":
        thisActivity['category'] = 'even'
        thisActivity['message'] = "You cannot gamble without gold!"
    elif (request.session['gold']+randGold) < 0:
        thisActivity['category']  = 'loss'
        thisActivity['message'] = "You lost all your money at the Casino! "#add time if possible
        request.session['gold'] = 0
    elif building == "Casino" and randGold < 0:
        thisActivity['category'] = 'loss'
        thisActivity['message'] = "You Lost " +str(abs(randGold)) + " from the Casino! "#add time if possible
        request.session['gold'] += randGold
    else:
        thisActivity['category'] = 'win'
        thisActivity['message'] = "You Earned " +str(randGold) +" from the " + building +"! "#add time if possible
        request.session['gold']+= randGold
    
    addActivity(request, thisActivity)

    return redirect('/')

def reset(request):
    request.session.pop('activity')
    request.session.pop('gold')
    return redirect('/')

def addActivity(request, act):
    tempAct = request.session['activity']
    tempAct.append(act)
    request.session['activity']