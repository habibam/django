# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
from models import Book, Author

# Create your views here.
def main(request):
    return HttpResponse("""



Books and Authors go here







""")