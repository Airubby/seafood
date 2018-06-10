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

@csrf_exempt
def test_api(request):
    print("222")
    if request.method=="GET":
        return HttpResponse(json.dumps({"success":True,"err":'注册成功！'}))
    elif request.method=="POST":
        return HttpResponse(json.dumps({"success": False, "err": '注册成功！'}))

@csrf_exempt
def register(request):
    print("123")
    if request.method=="POST":
        # 接受用户输入
        username = request.POST.get('username')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        email = request.POST.get('email')

        # 判断两次密码
        if password != cpassword:
            return HttpResponse(json.dumps({"success":False,"err":'两次密码一不一样！'}))

        # 密码加密
        # md5=hashlib.md5()
        # md5.update(password.encode("utf8"))
        # tpassword = md5.hexdigest()

        # 创建对象
        user = models.UserInfo()
        user.username = username
        user.password = password
        user.email = email
        user.save()
        # 注册成功，转到登录页面
        return HttpResponse(json.dumps({"success":True,"err":'注册成功！'}))
    elif request.method=="GET":
        print('2222')
        return HttpResponse(json.dumps({"success": True, "err": '注册成功！'}))
