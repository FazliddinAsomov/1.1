from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello world. You're main page</h1>")


def about(request):
    return HttpResponse("<h1>hello world. You're about page</h1>")