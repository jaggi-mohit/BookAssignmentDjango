"""Assignment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Customer import views as v1
from Seller import views as v2
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',v1.Signup,name="signup"),
    path('login',v1.Login,name="login"),
    path('home',v1.home,name="home"),
    path('profile',v1.profile,name='profile'),
    path('update',v1.update,name="update"),
    path('seller',v2.seller,name="seller"),
    path('sellerhome',v2.sellerhome,name="sellerhome"),
    path('tprofile',v2.tprofile,name='tprofile'),
    path('addbook',v2.addbook,name="addbook"),
    path('edit/<str:pk>',v2.edit,name="edit"),
    path('del/<str:pk>',v2.delete,name="del"),
    path('add',v2.add,name="add"),
    path('myorder',v2.myorder,name="myorder"),
    path('logout',v2.logout,name='logout'),
    path('delete/<str:pk>',v2.delete1,name="delete"),
    path('orderdetail',v2.orderdetail,name="orderdetail"),
    path('search',v2.search,name='search'),
   
    
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)