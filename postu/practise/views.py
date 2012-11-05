# Create your views here.
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse
from wrapper import *
import Image
import os.path


def grid(request):
    return render_response(request, "practise/gridTest.html")

def bootStrap(request):
    return render_response(request, "practise/bootstrap.html")

def _resized(image, new_w, new_h):
    img_w , img_h = image.size
   
    target_rate = new_w / new_h
    img_rate = img_w / img_h
    if ( img_rate > target_rate ):
        thumb_w = new_w
        thumb_h = new_w / img_rate
    else:
        thumb_h = new_h
        thumb_w = new_h * img_rate
        
    print thumb_w, thumb_h
    return image.resize((thumb_w, thumb_h), Image.BILINEAR)  

def upload_img(request):
    return render_response(request, "practise/upload_img.html")


def upload(request):
    reqfile = request.FILES['file']
    new_w = 600
    new_h = 400
    image = Image.open(reqfile)
    img_w , img_h = image.size
    #print img_w , img_h
    #image.thumbnail((128,128),Image.ANTIALIAS)
    thumb = _resized(image, new_w, new_h)
    projectRoot = os.path.abspath('.').replace('\\','/')
    thumb.save(projectRoot + "/static/thumb/1.jpeg","JPEG")
    return render_response(request, "practise/upload_img.html")



