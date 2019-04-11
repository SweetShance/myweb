from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.models import User
from .forms import LoginForm, RegisterForm
from .utils import statistical


def login_utils(request):
    # 注册
    if request.method == "POST":
        registerform = RegisterForm(request.POST)
        if registerform.is_valid():
            username = registerform.cleaned_data['username']
            password = registerform.cleaned_data['password']
            email = registerform.cleaned_data['email']

            # 创建用户
            User.objects.create_user(username=username, email=email, password=password)
            # 登录
            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)
    #登录
    if request.method == "POST":
        #接收数据
        loginform = LoginForm(request.POST)
        if loginform.is_valid():
            user = loginform.cleaned_data["user"]
            auth.login(request, user)
    else:
        loginform = LoginForm()
        registerform = RegisterForm()
    context = {
        "loginform": loginform,
        "registerform": registerform,
    }
    return context

def logout_view(request):
    urlform = request.META.get('HTTP_REFERER', reverse('index'))
    auth.logout(request)
    return redirect(urlform)

def index(request):
    context = login_utils(request)

    st_context = statistical(request)
    for key, value in st_context.items():
        context[key] = value
    return render(request, 'index.html', context)

