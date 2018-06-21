from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world! it's my first django2 project!")

# Create your views here.
