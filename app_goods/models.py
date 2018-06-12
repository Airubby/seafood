from django.db import models
from tinymce.models import HTMLField
#ImageField：pip install Pillow
# Create your models here.

class TypeInfo(models.Model):
    title=models.CharField(max_length=20)
    isDelete=models.BooleanField(default=False)

class GoodsInfo(models.Model):
    title=models.CharField(max_length=20)
    pic=models.ImageField(upload_to="app_goods")
    price=models.DecimalField(max_digits=5,decimal_places=2)
    isDelete=models.BooleanField(default=False)
    unit=models.CharField(max_length=20)
    click=models.IntegerField()
    description=models.CharField(max_length=200)
    store=models.IntegerField()
    content=HTMLField()
    type=models.ForeignKey(to = "TypeInfo", to_field = 'id', on_delete = models.CASCADE)
    recommend=models.BooleanField(default=False)