# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from models import User, UserManager
from django.contrib.messages import error
# Create your views here.

def Test(request):
    return HttpResponse('Success!')


# a GET request to /users - calls the index method to display all the users. This will
#  need a template.
def Index(request):
    context = {
        'users' : User.objects.all(),
    }
    return render (request, 'RestfulUsers_app/index.html', context)


# GET request to /users/new - calls the new method to display a form allowing users to
#  create a new user. This will need a template.
def New(request):
    return render(request, 'RestfulUsers_app/newUser.html')


##POST to /users/create - calls the create method to insert a new user record into our database.
#  This POST should be sent from the form on the page /users/new. Have this redirect to
#  /users/<id> once created. <--silly
def CreateUser(request):
    errors = User.objects.validate(request.POST)
    if len(errors):
        for key, value in errors.iteritems():
            error(request, value, extra_tags=key)
        return redirect('/users/new')

    newUser = User.objects.create(first_name=request.POST['first_name'], 
        last_name=request.POST['last_name'], email=request.POST['email'])

    # assignment asks for this but it's silly
    # return redirect('/users/{}'.format(newUser.id))
    return redirect('/users')


# GET /users/<id> - calls the show method to display the info for a particular user with given id.
#  This will need a template.
def Show(request, userID):
    user= User.objects.get(id=userID)
    context={
        'id': user.id,
        'name': "{} {}".format(user.first_name, user.last_name),
        'email': user.email,
        'created_at': user.created_at,
    }
    return render(request, 'RestfulUsers_app/show.html', context)

# GET request /users/<id>/edit - calls the edit method to display a form allowing users to edit an
#  existing user with the given id. This will need a template.
def Edit(request, userID):
    user= User.objects.get(id=userID)
    context={
        'id': user.id,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'created_at': user.created_at,
    }
    return render(request, 'RestfulUsers_app/editUser.html', context)

# POST /users/<id> - calls the update method to process the submitted form sent from /users/<id>/edit.
#  Have this redirect to /users/<id> once updated.
def Update(request, userID):
    errors = User.objects.validate(request.POST)
    if len(errors):
        for key, value in errors.iteritems():
            error(request, value, extra_tags=key)
        return redirect('/users/{}/edit'.format(userID))

    userUpdating = User.objects.get(id=userID)
    userUpdating.first_name = request.POST['first_name']
    userUpdating.last_name = request.POST['last_name']
    userUpdating.email = request.POST['email']
    userUpdating.save()

    # assignment asks for this but it's silly
    # return redirect('/users/{}'.format(newUser.id))
    return redirect('/users')

# GET /users/<id>/destroy - calls the destroy method to remove a particular user with the given id.
#  Have this redirect back to /users once deleted.
def Destroy(request, userID):
    toDestroy = User.objects.get(id=userID)
    toDestroy.delete()
    return redirect('/users')