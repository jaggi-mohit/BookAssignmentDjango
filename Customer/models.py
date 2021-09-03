from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import BooleanField


class Customer(models.Model):
    address=models.TextField()
    user=models.OneToOneField(User,on_delete=models.CASCADE,default="")
    mobile=models.IntegerField(null=True)
    ProfilePhoto=models.ImageField(upload_to='images',default="images\default.png")

    def __str__(self):
        return self.user.first_name


class BooksPurch(models.Model):
    BookName=models.CharField(max_length=20)
    Buyer=models.ForeignKey(User,on_delete=models.CASCADE,default="")
    Items=models.IntegerField(null=True)
    Price=models.IntegerField(null=True)
    BookImg=models.ImageField(upload_to='images',default="images\default.png")
    def __str__(self):
        return self.Buyer.first_name


class cart(models.Model):
    Items=models.IntegerField(null=True)
    Name=models.CharField(default="",max_length=20)
    users=models.ForeignKey(User,on_delete=models.CASCADE,default="")
    sum=models.IntegerField(null=True)
    Payed=BooleanField(default=False)
    
    def __str__(self):
        return self.Name