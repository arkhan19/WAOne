from django.contrib import admin
from django.urls import path
from WAOne import views
from Page import views as page
from Post import views as post

urlpatterns = [
    # URLs for Main
    path('', views.login),
]