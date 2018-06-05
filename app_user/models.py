from django.db import models

# Create your models here.

class UserInfo(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=40)
    email=models.CharField(max_length=30)
    phone=models.CharField(max_length=11,default='')
    receiver=models.CharField(max_length=20,default='')
    address=models.CharField(max_length=100,default='')
    #default,blank是python层面的约束，不影响数据库表结构