from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def create_post(request):
    return HttpResponse('CREATE YOUR POST')


def edit_post(request):
    return HttpResponse('EDIT YOUR POST')


def del_post(request):
    return HttpResponse('DELETE YOUR POST')