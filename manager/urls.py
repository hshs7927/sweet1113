from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all_item/', views.all_item, name='all_item'),
    
]