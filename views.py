from django.shortcuts import render
from django.http import HttpsResponse

#create your views here

def index(request):
    return HttpsResponse("<h1>Welcome</h1>")

def about(request):
    return HttpsResponse("<h1>About page</h1>")
