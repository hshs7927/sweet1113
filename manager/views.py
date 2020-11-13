from django.shortcuts import render, HttpResponse
from .models import Allitem, Store, Store_set, Today_lineup
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def index(request):
    #로그인한 유저의 마카롱매장이름 노출하는 방법?

    context = {   }
    return render(request, 'manager/index.html', context)


def all_item(request):
    #모든아이템 보여주기 
    return HttpResponse("모든아이템")