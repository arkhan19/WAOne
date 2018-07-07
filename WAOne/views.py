from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('HOME')


def login(request):
    return HttpResponse('LOGIN')


def logout(request):
    return HttpResponse('LOGOUT')