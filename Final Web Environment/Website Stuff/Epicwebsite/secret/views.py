from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, this is the secret index I guess ._.")
