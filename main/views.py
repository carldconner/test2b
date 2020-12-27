from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(response):
    return HttpResponse("<H1>This is Test 2</H1>")

def v1(response):
    return HttpResponse("<H1>View 1 test</H1>")
