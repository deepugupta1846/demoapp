from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Home(self):
    return HttpResponse('Hello world')