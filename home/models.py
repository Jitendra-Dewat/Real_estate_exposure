from django.db import models
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=100)
    content = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'Message From '+ self.name + ', Email: ' + self.email

class Profiledetail(models.Model):
    email = models.OneToOneField(User, to_field="username",unique=True, on_delete=models.CASCADE,default=" ")
    firstname = models.CharField(max_length=255, default="")
    middlename = models.CharField(max_length=255, default="")
    lastname = models.CharField(max_length=255, default="")
    dob = models.CharField(max_length=255, default="")
    gender = models.CharField(max_length=255, default="")
    phone = models.CharField(max_length=255, default="")
    address = models.CharField(max_length=255, default="")
    address2 = models.CharField(max_length=255, default="")
    country = models.CharField(max_length=50, default="")
    statename = models.CharField(max_length=50, default="")
    city = models.CharField(max_length=70, default="")
    zipf = models.CharField(max_length=6, default="")
    image = models.ImageField(upload_to='home/userprofiles', default="")

    

    def __str__(self):
       return ' Email : ' + str(self.email) + ' , Name : ' + self.firstname


