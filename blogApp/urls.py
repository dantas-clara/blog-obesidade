from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from blogApp import views

urlpatterns = [
    path('', views.index, name='index'),
]


