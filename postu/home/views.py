# Create your views here.
from django.http import HttpRequest
from wrapper import *


def main(request, page="home"):
    navlist = ['home', 'about', 'contact', 'test test']
    return render_response(request, 'home/%s.html' %page , {'navlist': navlist, 'page': page} )

def test(request):
    #print request.REMOTE_ADDR
    return render_response(request, "home/index.html")
