# Create your views here.
from django.http import HttpRequest
from wrapper import *

def main(request):
    #print request.REMOTE_ADDR
    return render_response(request, "home/index.html")