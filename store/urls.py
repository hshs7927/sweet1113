  
from django.contrib import admin
from django.urls import path
from . import views

app_name= 'store'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('order_detail/', views.order_detail, name='order_detail'),
    path('order_history/', views.order_history, name='order_history'),  

]