from django.db import models
from django.contrib.auth.models import User

class Seller(models.Model):
    address=models.TextField()
    user=models.OneToOneField(User,on_delete=models.CASCADE,default="")
    mobile=models.CharField(max_length=10,default="")
    ProfilePhoto=models.ImageField(upload_to='images',default="images\default.png")
    IsSeller=models.BooleanField(default=False)

    def __str__(self):
        return self.user.first_name


class SellerBooks(models.Model):
    BookName1=models.CharField(max_length=20)
    Buyers=models.CharField(max_length=20)
    Seller=models.ForeignKey(User,on_delete=models.CASCADE,default="")
    Price=models.IntegerField(null=True)
    BookImg=models.ImageField(upload_to='images',default="images\default.png")
    BuyerAddr=models.TextField(default="")
    Mobile=models.CharField(max_length=10,default="")
    Items=models.IntegerField(null=True)
    unique=models.BooleanField(default=False)
    def __str__(self):
        return self.Seller.first_name