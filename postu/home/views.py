# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse 
from postu import settings

def main(request):
    
    return render_to_response("home/main.html")
#    return HttpResponse(settings.STATICFILES_ROOT)