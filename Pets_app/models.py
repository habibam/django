# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..LoginReg_app.models import User
import re

NAME_REGEX = re.compile(r"(^[a-zA-Z\-]+$)")

# Create your models here.
class PetManager(models.Manager):
    def createPet(self, postData):
        tempPet = self.create(
            name = postData['pet_name'],
            kind = postData['kind'],
            owner = User.objects.get(id=postData['currentUser'])
        )

        return tempPet

    def validatePet(self, postData):
        results ={'status': True, 'errors': []}
        
        if len(postData['pet_name']) < 2:
            results['status'] = False
            results['errors'].append('Pet names must be at least 2 characters')

        if not re.match(NAME_REGEX, postData['pet_name']):
            results['status'] = False
            results['errors'].append('Pet names may not contain special characters')

        return results


class Pet(models.Model):
    name = models.CharField(max_length=255)
    kind = models.CharField(max_length=255)
    owner = models.ForeignKey(User, related_name='pets')
    objects = PetManager()