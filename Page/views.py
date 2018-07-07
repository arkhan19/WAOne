from django.shortcuts import render
from django.http import HttpResponse

# Page is like Profile for Each User consisting of list view of all posts.
# Create your views here.


def create_page(request):
    return HttpResponse('CREATE YOUR PAGE')


def edit_page(request):
    return HttpResponse('EDIT YOUR PAGE')


def del_page(request):
    return HttpResponse('DELETE YOUR PAGE')