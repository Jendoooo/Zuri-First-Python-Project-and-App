from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("Well, I just created this repnonse."
                         "Let's see what we get")
