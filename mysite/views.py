from os import rename
from django import http
from django.http import HttpResponse
from django.shortcuts import render

def home_view(request):
    return render(request,'homepage.html')

