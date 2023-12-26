from django.db import models

# Create your models here.
class student(models.Model):
    FirstName=models.CharField(max_length=30)
    LastName=models.CharField(max_length=30)
    age=models.IntegerField(default=123456)
    email=models.EmailField(max_length=30)
    phone=models.IntegerField()
    address=models.TextField(max_length=50)
    gender=models.CharField(max_length=30)
    place=models.CharField(max_length=30)
    course=models.CharField(max_length=30)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    value=models.IntegerField(default=1234)
    usertype=models.CharField(max_length=30,default=3452)


class teacher(models.Model):
    FirstName=models.CharField(max_length=30)
    LastName=models.CharField(max_length=30)
    age=models.IntegerField()
    email=models.EmailField(max_length=30)
    phone=models.IntegerField()
    address=models.TextField(max_length=50)
    gender=models.CharField(max_length=30,default=76543)
    place=models.CharField(max_length=30)
    department=models.CharField(max_length=30)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    value=models.IntegerField(default=5678)
    usertype=models.CharField(max_length=30,default=7896)