# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
# Create your views here.
from userlogin import settings
from . import models
import hashlib


# def my_view(request):
#     if not request.user.is_authenticated():
#         return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

def hash_code(s, salt='mysite'):  # 加点盐
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())  # update方法只接收bytes类型
    return h.hexdigest()


def index(request):
    return render(request, 'login/index.html')


def login(request):
    # 如果登录了就进入首页
    if request.session.get('is_login', None):
        return redirect('/index/')
    if request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        if username and password:
            username = username.strip()
            try:
                user = models.User.objects.get(name=username)
                if user.password == hash_code(password):
                    # 往session字典内写入用户状态和数据：
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    return redirect('/index')
                else:
                    message = "密码不正确"
            except:
                message = "用户不存在!"
            return render(request, 'login/login.html', {'message': message})

    return render(request, 'login/login.html')


def register(request):
    # 如果是登录的就进入首页
    if request.session.get('is_login', None):
        return redirect('/index/')
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password1 = request.POST.get('password1', None)
        password2 = request.POST.get('password2', None)
        email = request.POST.get('email', None)
        gender = request.POST.get('gender', None)
        if password1 != password2:
            message = "两次输入的密码不同！"
            return render(request, 'login/register.html', {'message': message})
        else:
            same_name = models.User.objects.filter(name=username)
            if same_name:
                message = '该用户名已存在，请重新输入用户名！'
                return render(request, 'login/register.html', {'message': message})
            same_email = models.User.objects.filter(email=email)
            if same_email:
                message = '该邮箱地址已被注册，请使用别的邮箱！'
                return render(request, 'login/register.html', {'message': message})

            user = models.User.objects.create(name=username, password=hash_code(password1), email=email, sex=gender)
            request.session['is_login'] = True
            request.session['user_id'] = user.id
            request.session['user_name'] = user.name
            return redirect('/index')

    return render(request, 'login/register.html')


def logout(request):
    if not request.session.get('is_login', None):
        return redirect('/index')
    # 清空所有session
    request.session.flush()
    return redirect("/index/")


def userblog(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    return render(request, 'login/userblog.html')
