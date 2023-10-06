from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    # use request as parameter when rendering, eventhough its not render, its fine
    return HttpResponse('Hello world!')
