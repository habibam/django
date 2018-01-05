# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
from django.db import models

# Create your models here.
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-z]+$')

class UserManager(models.Manager):
    def validate(self, post):
        errors={}

        for key, value in post.iteritems():
            if len(value) < 1:
                errors[key]="{} field is required".format(key.replace('_', ''))
        if not 'email' in errors and not re.match(EMAIL_REGEX, post['email']):
            errors['key'] ='Invalid email'
        else:
            if len(self.filter(email=post['email'])) > 1:
                errors['email'] = 'Email already in use'
        return errors


class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length = 255)
    created_at = models.DateField(auto_now_add=True)
    objects = UserManager()