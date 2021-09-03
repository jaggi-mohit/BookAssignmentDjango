from django.contrib import messages
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User , auth
from .models import BooksPurch, Customer
from Seller.models import SellerBooks,Seller
from django.core.files.storage import FileSystemStorage
def Signup(request):
    if request.method == "POST":
        fname=request.POST['name1']
        lname=request.POST['name2']
        address=request.POST['addr']
        email=request.POST['email']
        passw=request.POST['password']
        

        if User.objects.filter(username=email):
            messages.error(request,f'Email Already Exists!Try Another or Login!')
            return redirect('signup')
        
        else:
            adduser=User.objects.create_user(username=email,password=passw,first_name=fname,last_name=lname,is_staff=True)
            auth.login(request,adduser)
            x= request.user
            custmr=Customer(address=address,user_id=x.id)
            custmr.save()
            
            z=request.user.first_name

            messages.success(request,f'Welcome {z}! Account Created Kindly Login!')
            return redirect('login')
        
        

    
    return render(request,'Signup.html')

def Login(request):
    if request.method=="POST":
        mail=request.POST['Email']
        passw1=request.POST['password']
        user=auth.authenticate(username=mail,password=passw1)

        print(user)
        if user is not None:
            auth.login(request,user)
            x = request.user
            try:
                isteach= Seller.objects.get(user_id=x.id)
                if isteach.IsSeller == True:
                    messages.info(request,f'Kindly Login from Seller Login!')
                    return redirect('login')

                else:
                    auth.logout(request)
                    messages.info(request,f'You are not assigned as Seller by admin!')
                    return redirect('login')

            except:
                return redirect('home')

            
        else:
            messages.error(request,f'Invalid Credentials!Try Again!')
            return redirect('login')
    else:

        return render(request,'login.html')


def home(request):
    user1=request.user
    if request.user.is_anonymous:
        messages.info(request,f'Kindly Login!')
        return redirect('login')
    if user1 is not None:
        print(user1.id)
        print(request.user)
        n= SellerBooks.objects.all()
        return render(request,'home.html',{'data':n})

def profile(request):
    if request.method == "POST" and request.FILES['myfiles']:
        myfiles=request.FILES['myfiles']
        fs= FileSystemStorage()
        filename=fs.save(myfiles.name,myfiles)
        url=fs.url(filename)
        uid=request.user
        t = Customer.objects.get(user_id=uid.id)
        t.ProfilePhoto=url
        t.save()
    data = Customer.objects.filter(user_id=request.user.id)
    return render(request,'profile.html',{'data':data})

def update(request):
    if request.method == 'POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        addrs=request.POST['addrs']
        mail=request.POST['mail']
        mob=request.POST['mob']
        x = request.user
        y= Customer.objects.get(user_id=x.id)
        y.address=addrs
        y.mobile=mob
        y.save()
        usr=User.objects.get(username=x)
        usr.first_name=fname
        usr.last_name=lname
        usr.save()

        return redirect('profile')