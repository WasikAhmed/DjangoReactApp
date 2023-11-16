from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def main(response):
    return HttpResponse("<h1>Hello</h1>")

