from django.db import models

# Create your models here.
class shopvegdb(models.Model):
    VegitableName = models.CharField(max_length=50, null=True, blank=True)
    Price = models.IntegerField(null=True, blank=True)
    Description = models.CharField(max_length=500, null=True, blank=True)
    Image = models.ImageField(upload_to="profile")

class fruitsdb(models.Model):
    FruitsName = models.CharField(max_length=50, null=True, blank=True)
    Price = models.IntegerField(null=True, blank=True)
    Description = models.CharField(max_length=500, null=True, blank=True)
    Image = models.ImageField(upload_to="profile")


class admindb(models.Model):
    Name = models.CharField(max_length=50,null=True,blank=True)
    MobileNumber = models.IntegerField(null=True,blank=True)
    EmailID = models.EmailField(null=True,blank=True)
    Image = models.ImageField(upload_to="profile")
    UserName = models.CharField(max_length=50,null=True,blank=True)
    Password = models.CharField(max_length=50,null=True,blank=True)
    ConfirmPassword = models.CharField(max_length=50,null=True,blank=True)

class categorydb(models.Model):
    CategoryName = models.CharField(max_length=50, null=True, blank=True)
    Description = models.CharField(max_length=500, null=True, blank=True)
    Image = models.ImageField(upload_to="profile")

class productdb(models.Model):
   CategoryName = models.CharField(max_length=50, null=True, blank=True)
   ProductName = models.CharField(max_length=50, null=True, blank=True)
   Price = models.IntegerField(null=True, blank=True)
   Description = models.CharField(max_length=500, null=True, blank=True)
   Image = models.ImageField(upload_to="profile")

class Contactdatab(models.Model):
    Name = models.CharField(max_length=50, null=True, blank=True)
    EmailID = models.EmailField(null=True, blank=True)
    Subject = models.CharField(max_length=50, null=True, blank=True)
    Message = models.CharField(max_length=50, null=True, blank=True)
