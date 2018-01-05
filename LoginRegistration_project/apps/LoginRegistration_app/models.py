# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re

# Create your models here.
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r"^(?=.*[A-Za-z])[A-Za-z\d ]{8,}$")

class UserManager(models.Manager):
    def validate(self, postData):
        errors = []
        #####check for name length
        if len(postData['first_name']) < 2:
            errors.append('First Name must be 2 or more characters')

        if len(postData['last_name']) < 2:
            errors.append('Last Name must be 2 or more characters')

        #####check for weirdo characters in name
        if not re.match(NAME_REGEX, postData['first_name']) or not re.match(NAME_REGEX, postData['last_name']):
            errors.append('Names may not contain special characters')

        #####check for valid email
        if not re.match(EMAIL_REGEX, postData['email']):
            errors.append('Invalid email')

        #####check if email is in use
        if len(self.filter(email=postData['email'])) > 1:
            errors.append('Email already in use')

        #####check for password length
        if len(postData['password']) < 8:
            errors.append('Passwords must be 8 or more characters')

        #####check for valid characters
        if not re.match(PASSWORD_REGEX, postData['password']):
            errors.append('Passwords may only contain leters, digits, and spaces')

        #####check that passwords match
        if postData['password'] != postData['password_confirm']:
            errors.append("Passwords don't match")

        return errors

    def validate_login(self, postData):
        errors = []
        if len(self.filter(email=postData['login_email'])) < 1:
            errors.append('Invalid Email')
            return errors
        else:
            user = self.filter(email=postData['login_email'])[0]
            print user
            if postData['login_password'] != user.password:
                errors.append('Incorrect password or email')
        return errors


class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length=255)
    birthday = models.DateField()
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()