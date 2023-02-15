from django.contrib import admin
from django.urls import path
from djangoprj.views import index

urlpatterns = [
    path('index', index)
]