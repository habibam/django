# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=2500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        if __name__ == '__main__':
            return "<Book: {} -- {} | Authors:{}>".format(self.name, self.desc, self.authors.all())##doesn't work
        else:
            return "<Book: {} -- {}>".format(self.name, self.desc)

class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    books = models.ManyToManyField(Book, related_name="authors")
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        if __name__ == '__main__':
            return "<Author: {} {} ({}) | Books: {}>".format(self.first_name, self.last_name, self.email, self.books.all())##doesn't work
        else:
            return "<Author: {} {} ({})>".format(self.first_name, self.last_name, self.email)