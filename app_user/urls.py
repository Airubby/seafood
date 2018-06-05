#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author:Airubby 
@file: urls.py 
@time: 2018/06/05 
"""


from django.conf.urls import url
from django.urls import re_path
from app_user import views

urlpatterns=[
re_path('register/$', views.register),
re_path('register_exist/$', views.register_exist),
re_path('login/$', views.login),
]



