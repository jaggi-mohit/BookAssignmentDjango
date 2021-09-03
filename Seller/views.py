from django.contrib import messages
from django.db.models.aggregates import Sum
from django.db.models import Q
from django.db.models.fields import NullBooleanField
from django.shortcuts import render,HttpResponse,redirect
from django.db.models import Q
from django.contrib.auth.models import User , auth
from .models import Seller,SellerBooks
from Customer.models import BooksPurch, Customer, cart
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required

def seller(request):
    if request.method=="POST":
        mail=request.POST['Email']
        passw1=request.POST['password']
        user=auth.authenticate(username=mail,password=passw1)

        print(user)
        if user is not None:
            auth.login(request,user)
            x = request.user
            try:
                isSeller= Seller.objects.get(user_id=x.id)
                if isSeller.IsSeller == True:
                    return redirect('sellerhome')

                else:
                    auth.logout(request)
                    messages.info(request,f'You are not assigned as seller by admin yet!')
                    return redirect('seller')

            except:
                messages.info(request,f'Kindly Login from Customer Login!')
                return redirect('login')
                

            
        else:
            messages.error(request,f'Invalid Credentials!Try Again!')
            return redirect('seller')
    return render(request,'sellerlog.html')

@login_required(login_url='login')
def sellerhome(request):
    x=SellerBooks.objects.filter(Seller_id=request.user.id)
    return render(request,'sellerhome.html',{'data':x})

@login_required(login_url='login')
def tprofile(request):
    if request.method == "POST" and request.FILES['myfiles']:
        myfiles=request.FILES['myfiles']
        fs= FileSystemStorage()
        filename=fs.save(myfiles.name,myfiles)
        url=fs.url(filename)
        uid=request.user
        t = Seller.objects.get(user_id=uid.id)
        t.ProfilePhoto=url
        t.save()
    data = Seller.objects.filter(user_id=request.user.id)
    return render(request,'tprofile.html',{'data':data})

def addbook(request):
    if request.method == "POST" and request.FILES['myfiles']:
        myfiles=request.FILES['myfiles']
        bname=request.POST['bname']
        bookp=request.POST['bookp']
        fs= FileSystemStorage()
        filename=fs.save(myfiles.name,myfiles)
        url=fs.url(filename)
        uid=request.user
        t = SellerBooks(BookImg=url,BookName1=bname,Price=bookp,Seller_id=uid.id,unique=True)
        t.save()
        
        t.save()

    return redirect('sellerhome')

def delete(request,pk):
    x= SellerBooks.objects.get(id=pk)
    x.delete()
    return redirect('sellerhome')

def edit(request,pk):

    if request.method == "POST" and request.FILES['myfiles']:
        myfiles=request.FILES['myfiles']
        bname=request.POST['bname']
        bookp=request.POST['bookp']
        fs= FileSystemStorage()
        filename=fs.save(myfiles.name,myfiles)
        url=fs.url(filename)
        uid=request.user
        t = SellerBooks.objects.get(id=pk)
        t.BookImg=url
        t.BookName1=bname
        t.Price=bookp
        t.save()
        return redirect('sellerhome')
        
    x= SellerBooks.objects.filter(id=pk)
    return render(request,'edit.html',{"x":x})

def add(request):
    if request.method =="POST":
        pk =request.POST['subm']
        x= SellerBooks.objects.get(id=pk)
        
        print(pk,"fgjhdfdj")
        y=x.BookName1
        z=x.BookImg
        k=x.Price
        c=x.Seller
    
        try:
            ss=cart.objects.get(users_id=request.user.id,id=pk)
            ss.Items +=1
            ss.sum=(k*ss.Items)
            ss.save()
            
        except:  
            kk=cart(Items=1,Name=y,users_id=request.user.id,id=pk,sum=k)
            kk.save()
    
    sum=cart.objects.filter(users_id=request.user.id).aggregate(Sum('sum'))
    sm=list(sum.values())[0]
    print(sm)
    dt=cart.objects.filter(users_id=request.user.id)
    
    return render(request,'cart.html',{'dt':dt,'sum':sm})


def myorder(request):
    if request.method=='POST':
        
        ord=cart.objects.filter(users_id=request.user.id).update(Payed=True)
        ord2=cart.objects.filter(users_id=request.user.id)
        s=Customer.objects.get(user_id=request.user.id)
        if s.mobile==None:
            messages.info(request,f'Kindly Update Your Mobile Number in Profile!')
            return redirect('profile')

        for i in ord2:
            x=BooksPurch(BookName=i.Name,Buyer_id=request.user.id,Items=i.Items,Price=i.sum)
            x.save()
            
            y=SellerBooks.objects.get(id=i.id)
            if y.Buyers !="":
                if y.Buyers ==request.user.username:
                    y.Buyers=request.user.username
                    y.Items=i.Items+y.Items
                    y.BuyerAddr=s.address
                    y.Mobile=s.mobile
                    y.Price=y.Price+i.sum
                    y.save()
                else:
                    z=SellerBooks(BookName1=y.BookName1,Seller=y.Seller,Buyers=request.user.username,Price=y.Price,BuyerAddr=s.address,Mobile=s.mobile,Items=1)
                    z.save()
            else:
                if y.Items==None:
                    y.Items=1
                else:
                    y.Items=i.Items+y.Items
                y.Buyers=request.user.username
                y.BuyerAddr=s.address
                y.Mobile=s.mobile
                y.save()


        cart.objects.all().delete()
        

    ord=BooksPurch.objects.filter(Buyer_id=request.user.id)
    
    return render(request,'myorder.html',{'dt':ord})



def logout(request):
    auth.logout(request)
    messages.info(request,f'Logged Out Successfully!')
    return redirect('login')

def delete1(request,pk):
    x= cart.objects.get(id=pk)
    x.delete()
    return redirect('add')

def orderdetail(request):
    x= SellerBooks.objects.filter(Seller_id=request.user.id)
    return render(request,'orderdetail.html',{'dt':x})


def search(request):
    if request.method=="POST":
        name=request.POST['search']
        if name == "":
            return redirect('home')
        x=SellerBooks.objects.filter(Q(BookName1__contains=name))
        return render(request,'home.html',{'data':x})

