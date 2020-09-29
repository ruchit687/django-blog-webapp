from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('<h1>Blog Home</h1>')
    # we can send complete html structure here but that will be messy,
    # so we create templates (by default django looks fro a templates sub directory & each of our installed apps)


def about(request):
    return HttpResponse('<h1>Blog About</h1>')
