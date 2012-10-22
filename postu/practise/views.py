# Create your views here.
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse
from wrapper import *
import Image


def upload_img(request):
    return render_response(request, "practise/upload_img.html")


def upload(request):    
    reqfile = request.FILES['file']
    print reqfile
    image = Image.open(reqfile)
    image.thumbnail((128,128),Image.ANTIALIAS)
    image.save("/home/projects/other/django/liangyihao/postu/static/thumb/1.jpeg","jpeg")
    return render_response(request, "practise/upload_img.html")
