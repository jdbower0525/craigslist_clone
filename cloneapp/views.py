from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

# Create your views here.


def view_index(request):
    return HttpResponse("YAY YOU MADE IT")
