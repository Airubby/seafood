#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author:Airubby 
@file: api.py 
@time: 2018/06/11 
"""


from django.shortcuts import render,redirect,HttpResponse
from app_user import models
import hashlib
import json
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def register(request):
    if request.method=="POST":
        print("post")
        data=json.loads(request.body.decode())
        print(data)
        # 接受用户输入
        username = data.get('username')
        password = data.get('password')
        cpassword = data.get('cpassword')
        email = data.get('email')
        # 判断两次密码
        if password != cpassword:
            return HttpResponse(json.dumps({"success":False,"msg":'两次密码一不一样！'}))

        # 密码加密
        md5=hashlib.md5()
        md5.update(password.encode("utf8"))
        tpassword = md5.hexdigest()

        #判断用户名存在
        count = models.UserInfo.objects.filter(username=username).count()
        print(count)
        if count>=1:
            return HttpResponse(json.dumps({"success": False, "msg": '用户名已经存在！'}))
        # 创建对象
        #models.UserInfo.objects.create(username=username, password=password,email=email)
        user = models.UserInfo()
        user.username = username
        user.password = tpassword
        user.email = email
        user.save()
        # 注册成功，转到登录页面
        return HttpResponse(json.dumps({"success":True,"msg":'注册成功！'}))
    elif request.method=="GET":
        pass


def login(request):
    if request.method=="POST":
        print("post")
        data=json.loads(request.body.decode())
        # 接受用户输入
        username = data.get('username')
        password = data.get('password')

        # 密码加密
        md5=hashlib.md5()
        md5.update(password.encode("utf8"))
        tpassword = md5.hexdigest()

        #判断用户名存在
        name = models.UserInfo.objects.filter(username=username).count()
        if name==0:
            return HttpResponse(json.dumps({"success": False, "msg": '用户名不存在！'}))

        #判断密码
        passw=models.UserInfo.objects.filter(password=tpassword).count()
        if passw==0:
            return HttpResponse(json.dumps({"success": False, "msg": '密码错误！'}))

        # 注册成功，转到登录页面
        return HttpResponse(json.dumps({"success":True,"msg":'登录成功！'}))