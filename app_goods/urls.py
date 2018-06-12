#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author:Airubby 
@file: urls.py 
@time: 2018/06/05 
"""


from django.urls import re_path
from app_goods import api

urlpatterns=[
    re_path('register$', api.register,name='register'),
    re_path('login', api.login,name='login'),
]



