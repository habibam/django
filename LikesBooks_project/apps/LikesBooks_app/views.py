# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

# Create your views here.
def main(request):
    return HttpResponse('Here be Likes and Books of future-past!')