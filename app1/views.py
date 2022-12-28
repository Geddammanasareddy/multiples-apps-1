from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return HttpResponse('MY NAME IS MANASA')
def second(request):
    return HttpResponse("<h1>my name is manasa")
