from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(response):
    return HttpResponse("<H1>You have reached page 1</H1>")

def v1(response):
    return HttpResponse("<H3>You are looking at an unauthorized view!</H3>")
