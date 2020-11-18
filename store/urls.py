  
from django.contrib import admin
from django.urls import path
from . import views

app_name= 'store'

urlpatterns = [
    path('', views.index, name='home'),
    path('<str:biz_url>', views.index, name='index'),
    path('new/<str:biz_url>', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('order_detail/<int:order_id>/', views.order_detail, name='order_detail'),
    path('<int:order_id>/delete/', views.delete, name='delete'),
    path('order_history/', views.order_history, name='order_history'),  
    path('review/<int:order_id>', views.review, name='review'),
    path('review_create/<int:order_id>', views.review_create, name='review_create'),
    #path('review/', views.review, name='review'),
    path('myprofile/', views.myprofile, name='myprofile'),
]