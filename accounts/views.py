from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from manager.models import Store



# Create your views here.
def sign_up(request):
    context = {}

    # POST Method
    if request.method == 'POST':
        if (request.POST['username'] and
                request.POST['password'] and
                request.POST['password'] == request.POST['password_check']):

            new_user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password'],
                first_name=request.POST['first_name'],
            )

            #사업자계정 추가정보 입력#
            new_storemember = Store(
                user = new_user,
                biz_name = request.POST['biz_name'],
                biz_num = request.POST['biz_num'],
                biz_url = request.POST['biz_url'],
                biz_insta = request.POST['biz_insta'],
                biz_address = request.POST['biz_address'],
                biz_tel = request.POST['biz_tel']
            )
            new_storemember.save()
            auth.login(request, new_user)
            return HttpResponse('정상적회원가입완료')

        else:
            context['error'] = '아이디와 비밀번호를 다시 확인해줴요.'

    # GET Method
    return render(request, 'accounts/sign_up.html', context)


def login(request):
    context = {}

    # POST Method
    if request.method == 'POST':
        if request.POST['username'] and request.POST['password']:

            user = auth.authenticate(
                request,
                username=request.POST['username'],
                password=request.POST['password']
            )

            if user is not None:
                auth.login(request, user)
                return HttpResponse("if user is not None이 트루라는 뜻")
            else:
                context['error'] = '아이디와 비밀번호를 다시 확인해주세요.'

        else:
            context['error'] = '아이디와 비밀번호를 모두 입력해주세요.'

    # GET Method
    return render(request, 'accounts/login.html', context)