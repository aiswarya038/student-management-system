from django.db import models

#student
class Student(models.Model):
    FirstName=models.CharField(max_length=30)
    LastName=models.CharField(max_length=30)
    # age=models.IntegerField(default=123456)
    email=models.CharField(max_length=30)
    phone=models.IntegerField()
    # address=models.CharField(max_length=50)
    place=models.CharField(max_length=30)
    # # course=models.CharField(max_length=30)
    # username=models.CharField(max_length=30)
    # password=models.CharField(max_length=30)

class Teacher(models.Model):
    FirstName=models.CharField(max_length=30)
    LastName=models.CharField(max_length=30)
    # age=models.IntegerField()
    email=models.CharField(max_length=30)
    phone=models.IntegerField()
    # address=models.CharField(max_length=50)
    place=models.CharField(max_length=30)
    # department=models.CharField(max_length=30)
    # username=models.CharField(max_length=30)
    # password=models.CharField(max_length=30)

