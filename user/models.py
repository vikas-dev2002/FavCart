from distutils.command.upload import upload
from tokenize import Name
from turtle import mode
from django.db import models

# Create your models here.
class contactus(models.Model):
    Name=models.CharField(max_length=100)
    Mobile=models.CharField(max_length=50)
    Email=models.CharField(max_length=50)
    Message=models.TextField()
    def __str__(self):
        return self.Name
###############################################################################
class category(models.Model):
    Name=models.CharField(max_length=48)
    CPic=models.ImageField(upload_to='static/category',null=True)
    def __str__(self):
        return self.Name    
##########################################################################################
class maincate(models.Model):
    Name=models.CharField(max_length=20)
    picture=models.ImageField(upload_to='static/mcategory/',null=True)
    cdate=models.DateField()
    def __str__(self):
        return self.Name
#############################################################################################
class myproduct(models.Model):
    pprice=models.FloatField()
    dprice=models.FloatField()
    psize=models.CharField(max_length=20)
    pcolor=models.CharField(max_length=20)
    pdes=models.TextField()
    pdel=models.CharField(max_length=60)
    ppic=models.ImageField(upload_to='static/category',default="")
    pdate=models.DateField()
    pcategory=models.ForeignKey(category,on_delete=models.CASCADE,null=True)
    mcategory=models.ForeignKey(maincate,on_delete=models.CASCADE,null=True)
#######################################################################################################
class register(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100,primary_key=True)
    mobile=models.CharField(max_length=30)
    ppic=models.ImageField(upload_to='static/profile',null=True)
    passwd=models.CharField(max_length=60)
    cpasswd=models.CharField(max_length=60)
    address=models.TextField()
######################################################################
class morder(models.Model):
    userid=models.CharField(max_length=70)
    pid=models.IntegerField()
    remarks=models.CharField(max_length=20)
    odate=models.DateField()
    status=models.BooleanField()
###################################################################################    
class mcart(models.Model):
    userid=models.CharField(max_length=70)
    pid=models.IntegerField()
    cdate=models.DateField()
    status=models.BooleanField()
#######################################################################################################3    


