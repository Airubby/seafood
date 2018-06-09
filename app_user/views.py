#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:Airubby
@file: urls.py
@time: 2018/06/05
"""

from django.shortcuts import render,redirect,HttpResponse
from app_user import models
import hashlib
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def register(request):
    if request.method == "GET":
        return render(request,'app_user/register.html')
    elif request.method=="POST":
        # 接受用户输入
        post = request.POST
        username = post.get('user_name')
        password = post.get('pwd')
        cpassword = post.get('cpwd')
        email = post.get('email')

        # 判断两次密码
        if password != cpassword:
            return redirect('/user/register/')

        # 密码加密
        md5=hashlib.md5()
        md5.update(password.encode("utf8"))
        tpassword = md5.hexdigest()

        # 创建对象
        user = models.UserInfo()
        user.username = username
        user.password = tpassword
        user.email = email
        user.save()
        # 注册成功，转到登录页面
        return redirect('/user/login/')

def register_exist(request):
    username=request.GET.get('username')
    count=models.UserInfo.objects.filter(username=username).count()
    print(count)
    return HttpResponse(json.dumps({'count':count}))

@csrf_exempt
def login(request):
    if request.method == "GET":
        username=request.COOKIES.get('username','') #cookies有就用username，没有就用空
        context={'error_name':'','error_pwd':'','username':username,'password':''}
        return render(request,'app_user/login.html',context)
    elif request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('pwd')
        jizhu=request.POST.get('jizhu',0)  #前端勾选了就获取jizhu的值1，没有就用默认值0
        users=models.UserInfo.objects.filter(username=username)

        if len(users)==1:
            md5 = hashlib.md5()
            md5.update(password.encode("utf8"))
            tpassword = md5.hexdigest()
            if tpassword==users[0].password:
                red=redirect('/user/info/')
                if jizhu!=0:
                    red.set_cookie('username',username)
                else:
                    red.set_cookie('username','',max_age=-1) #max_age=-1立马过期，设置过期时间
                request.session['user_id']=users[0].id
                request.session['user_name']=username
                return red
            else:
                context={'error_name':'','error_pwd':'密码错误','username':username,'password':password}
                return HttpResponse(json.dumps(context))
        else:
            context = {'error_name': '用户名错误', 'error_pwd': '', 'username': username, 'password': password}
            return HttpResponse(json.dumps(context))


def info(request):
    print(243)
    user_email=models.UserInfo.objects.get(id=request.session['user_id']).email
    context={
        'user_email':user_email,
        'user_name':request.session['user_name']
    }
    return render(request,'app_user/user_center_info.html',context)


