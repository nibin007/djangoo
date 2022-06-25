from asyncio.windows_events import NULL
from tabnanny import verbose
from unicodedata import name
from django.db import models

class Students(models.Model):
    name=models.CharField(max_length=100,verbose_name='Student_name')
    age=models.IntegerField()
    phone=models.CharField(max_length=25)
    email=models.EmailField()
    address=models.CharField(max_length=28,default=NULL)
    
class Teacher(models.Model):
     name=models.CharField(max_length=100,verbose_name='Student_name')
     age=models.IntegerField()
class Books(models.Model):
    name=models.CharField(verbose_name='book name',max_length=100)
    price=models.IntegerField()
    author=models.CharField(max_length=100)
    class Meta:
        db_table='Book'
        