from django.db import models
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import datetime
from django.utils import timezone

# Create your models here.
class Postforselling(models.Model):
    ownerid = models.ForeignKey(User, to_field="username",unique=False, on_delete=models.CASCADE,default=" ")
    propertyid = models.AutoField(primary_key=True)
    address = models.CharField(max_length=255, default="")
    address2 = models.CharField(max_length=255, default="")
    country = models.CharField(max_length=50, default="")
    statename = models.CharField(max_length=50, default="")
    city = models.CharField(max_length=70, default="")
    zipf = models.CharField(max_length=6, default="")
    cunstructionyear = models.CharField(max_length=255, default="")
    parking = models.CharField(max_length=6,default=False)
    furnshid = models.CharField(max_length=6,default=False)
    ac = models.CharField(max_length=6,default=False)
    swimmingpool = models.CharField(max_length=6,default=False)
    description = models.CharField(max_length=700, default="")
    price = models.CharField(max_length=12, default="")
    area = models.CharField(max_length=20, default="0")
    dateposted = models.DateTimeField(auto_now_add=True, blank=True)
    propertytype =models.CharField(max_length=10, default="")
    mainimage = models.ImageField(upload_to='properties/forsale', default="")
    

    
    def __str__(self):
        return  str(self.propertyid) +',' + str(self.ownerid)+',' + str(self.propertytype)

class Imgesofproperties(models.Model):
    propertyid = models.ForeignKey(Postforselling,to_field="propertyid",  unique=False, on_delete=models.CASCADE,default=" ")
    imageid = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='properties/forsale', default="")
    propertytype =models.CharField(max_length=10, default="")

    def __str__(self):
        return str(self.propertyid) + ', Image Id = ' + str(self.imageid) + ', Property Type = ' + self.propertytype
        
# Create your models here.
class Soldproperties(models.Model):
    oldownerid = models.CharField(max_length=255, default="")
    propertyid = models.AutoField(primary_key=True)
    address = models.CharField(max_length=255, default="")
    address2 = models.CharField(max_length=255, default="")
    country = models.CharField(max_length=50, default="")
    statename = models.CharField(max_length=50, default="")
    city = models.CharField(max_length=70, default="")
    zipf = models.CharField(max_length=6, default="")
    cunstructionyear = models.CharField(max_length=255, default="")
    parking = models.CharField(max_length=6,default=False)
    furnshid = models.CharField(max_length=6,default=False)
    ac = models.CharField(max_length=6,default=False)
    swimmingpool = models.CharField(max_length=6,default=False)
    description = models.CharField(max_length=700, default="")
    price = models.CharField(max_length=12, default="")
    area = models.CharField(max_length=20, default="0")
    dateposted = models.DateTimeField(auto_now_add=True, blank=True)
    propertytype =models.CharField(max_length=10, default="")
    mainimage = models.ImageField(upload_to='properties/forsale', default="")
    solddate = models.DateTimeField(auto_now_add=True, blank=True)
    newownerid = models.CharField(max_length=255, default="")
    

    
    def __str__(self):
        return  str(self.propertyid) +',' + str(self.oldownerid)+',' + str(self.propertytype)+ ',' + str(self.newownerid)

class Postforrent(models.Model):
    ownerid = models.ForeignKey(User, to_field="username",unique=False, on_delete=models.CASCADE,default=" ")
    propertyid = models.AutoField(primary_key=True)
    address = models.CharField(max_length=255, default="")
    address2 = models.CharField(max_length=255, default="")
    country = models.CharField(max_length=50, default="")
    statename = models.CharField(max_length=50, default="")
    city = models.CharField(max_length=70, default="")
    zipf = models.CharField(max_length=6, default="")
    cunstructionyear = models.CharField(max_length=255, default="")
    parking = models.CharField(max_length=6,default=False)
    furnshid = models.CharField(max_length=6,default=False)
    ac = models.CharField(max_length=6,default=False)
    swimmingpool = models.CharField(max_length=6,default=False)
    description = models.CharField(max_length=700, default="")
    rentpermonth = models.CharField(max_length=12, default="")
    area = models.CharField(max_length=20, default="0")
    dateposted = models.DateTimeField(auto_now_add=True, blank=True)
    propertytype =models.CharField(max_length=10, default="")
    mainimage = models.ImageField(upload_to='properties/forsale', default="")
    maxallowedtanent = models.IntegerField(default=1)
    livingtanent = models.IntegerField(default=0)
    

    
    def __str__(self):
        return  str(self.propertyid) +',' + str(self.ownerid)+',' + str(self.propertytype)+',' + str(self.maxallowedtanent)+',' + str(self.livingtanent)



class Imgesofrentalproperties(models.Model):
    propertyid = models.ForeignKey(Postforrent,to_field="propertyid",  unique=False, on_delete=models.CASCADE,default=" ")
    imageid = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='properties/forrent', default="")
    propertytype =models.CharField(max_length=10, default="")

    def __str__(self):
        return str(self.propertyid) + ', Image Id = ' + str(self.imageid) + ', Property Type = ' + self.propertytype



class Serviceproviderprofile(models.Model):
    email = models.OneToOneField(User, to_field="username",unique=True, on_delete=models.CASCADE,default=" ")
    serviceproviderprofileid = models.AutoField(primary_key=True)
    regno = models.CharField(max_length=6, default="")
    name = models.CharField(max_length=150, default="")
    phone = models.CharField(max_length=12, default="")
    estyear = models.CharField(max_length=255, default="")
    address = models.CharField(max_length=255, default="")
    address2 = models.CharField(max_length=255, default="")
    country = models.CharField(max_length=50, default="")
    statename = models.CharField(max_length=50, default="")
    city = models.CharField(max_length=70, default="")
    zipf = models.CharField(max_length=6, default="")
    bio = models.CharField(max_length=750, default="")

    def __str__(self):
        return str(self.email) + ' ' + self.regno + ' ' + self.name

class Employees(models.Model):
    serviceproviderprofileid = models.ForeignKey(Serviceproviderprofile,to_field="serviceproviderprofileid",  unique=False, on_delete=models.CASCADE,default=" ")
    employeeid = models.AutoField(primary_key=True)
    prfilepic = models.ImageField(upload_to='home/employeeprofile', default="")
    firstname = models.CharField(max_length=255, default="")
    middlename = models.CharField(max_length=255, default="")
    lastname = models.CharField(max_length=255, default="")
    dob = models.CharField(max_length=255, default="")
    gender = models.CharField(max_length=255, default="")
    phone = models.CharField(max_length=12, default="")
    address = models.CharField(max_length=255, default="")
    address2 = models.CharField(max_length=255, default="")
    country = models.CharField(max_length=50, default="")
    statename = models.CharField(max_length=50, default="")
    city = models.CharField(max_length=70, default="")
    zipf = models.CharField(max_length=6, default="")
    bio = models.CharField(max_length=750, default="")
    charges = models.CharField(max_length=6, default="")
    worktype = models.CharField(max_length=50, default="")
    vacantstatus = models.CharField(max_length=6, default="")

    def __str__(self):
        return self.firstname + ' is Employee of ' + str(self.serviceproviderprofileid.email) + ' vacant status :  ' + self.vacantstatus + ' From :  ' + self.city


class Roommateprofile(models.Model):
    email = models.OneToOneField(User, to_field="username",unique=False, on_delete=models.CASCADE,default=" ")
    roommateprofileid = models.AutoField(primary_key=True)
    prfilepicfile = models.ImageField(upload_to='home/roommateuserprofile', default="")
    firstname = models.CharField(max_length=255, default="")
    middlename = models.CharField(max_length=255, default="")
    lastname = models.CharField(max_length=255, default="")
    dob = models.CharField(max_length=255, default="")
    gender = models.CharField(max_length=255, default="")
    phone = models.CharField(max_length=12, default="")
    address = models.CharField(max_length=255, default="")
    address2 = models.CharField(max_length=255, default="")
    country = models.CharField(max_length=50, default="")
    statename = models.CharField(max_length=50, default="")
    city = models.CharField(max_length=70, default="")
    zipf = models.CharField(max_length=6, default="")
    smoking = models.CharField(max_length=6, default="")
    alchohal = models.CharField(max_length=6, default="")
    nonvegitarian = models.CharField(max_length=6, default="")
    earlybird = models.CharField(max_length=6, default="")
    bio = models.CharField(max_length=750, default="")
    rent = models.CharField(max_length=15, default="")
    area = models.CharField(max_length=15, default="")
    propertytype = models.CharField(max_length=7, default="")
    mainimage = models.ImageField(upload_to='properties/roommateprofilepropertyimages', default="")
    maxtanent = models.CharField(max_length=2, default="")
    livingtanent = models.CharField(max_length=15, default="")
    expecteddescriptionofguy = models.CharField(max_length=750, default="")


    def __str__(self):
        return self.firstname + ' ' + self.lastname


class Roommateprofilepropimages(models.Model):
    roommateprofileid = models.ForeignKey(Roommateprofile,to_field="roommateprofileid",  unique=False, on_delete=models.CASCADE,default=" ")
    imageid = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='properties/roommateprofilepropertyimages', default="")
    propertytype = models.CharField(max_length=10, default="")

    def __str__(self):
        return str(self.roommateprofileid) + ' ' + self.propertytype










    