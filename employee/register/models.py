from turtle import position, title
from django.db import models
# Create your models here.

class positions(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    Address = models.CharField(max_length=300)
    Email=models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    emp_code= models.CharField(max_length=100)
    position = models.CharField(max_length=20)
