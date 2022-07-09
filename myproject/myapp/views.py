from enum import unique
from multiprocessing import context
import re
from typing import final
from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from numpy import product
from .models import DETAIL
from .models import Cart
from .models import about



# Create your views here.
@csrf_exempt
def register(request):
    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        mobile=request.POST['mobile']
        firstname=request.POST['lastname']
        lastname=request.POST['firstname']
        if User.objects.filter(email=email).exists():
            response_data = {'created': 'no2',}
            return JsonResponse(response_data)
        elif User.objects.filter(username=username).exists():
            response_data = {'created': 'no2',}
            return JsonResponse(response_data)
        else:
            user= User.objects.create_user(username=username,email=email,password=password)
            response_data = {'created': 'YES',}
            user.save()
            return JsonResponse(response_data)



        

    else:
        return render(request,'register.html')

@csrf_exempt    
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            response_data1 = {'created': 'YES',}
            
            return JsonResponse(response_data1)
        else:
            response_data1 = {'created': 'NO',}
            return JsonResponse(response_data1)
            
    else:
        return render(request,'login.html')
@csrf_exempt
def index(request):


    return render(request,"index.html")


    
@csrf_exempt
def logout(request):
    auth.logout(request)
    response_data1 = {'created': 'YES',}
    return JsonResponse(response_data1)
    
@csrf_exempt
def electronics(request):
    c="electronics"
    detail11=DETAIL.objects.filter(type = c ,final=0)
    print(detail11)
    detail12=DETAIL.objects.filter(type = c ,final=1)
    print(detail12)
    detail13=DETAIL.objects.filter(type = c ,final=2)
    context={'detail11':detail11,'detail12':detail12,'detail13':detail13}
    response_data1 = {'created': 'YES',}

    return render(request,"electronics.html",context)
def eatable(request):
    c="eatable"
    detail2=DETAIL.objects.filter(type = c)
    return render(request,"eatable.html",{"detail2":detail2})
@csrf_exempt
def grocery(request):
    response_data1 = {'created': 'YES',}
    c="grocery"
    detail3=DETAIL.objects.filter(type = c)
    return render(request,"grocery.html",{"detail3":detail3})
@csrf_exempt
def clothes(request):
    response_data1 = {'created': 'YES',}
    c="clothes"
    detail4=DETAIL.objects.filter(type = c)
    return render(request,"clothes.html",{"detail4":detail4})
@csrf_exempt
def cart(request):

    if request.method=='POST':  
        data = request.POST["detail"]
        data1= request.user.username
        obj=DETAIL.objects.get(product_name=data)
        if Cart.objects.filter(product_id =data ,userid = data1 ,unique=0 ).count() == 0:
            cart=Cart.objects.create(product_id=data,quantity=1,userid=request.user.username)
            
            cart.save()
        else:
            cart=Cart.objects.get(product_id =data,userid = data1,unique=0)
            cart.quantity=cart.quantity+1

            cart.save()
            print(cart)
        cart.total_cost=(cart.quantity)*(obj.price)
        cart.save()
        print(cart.total_cost)

        context={'ele':'ok'}
        
        return JsonResponse(context)
    else:
        c=Cart.objects.filter(userid=request.user.username,unique=0)
        b=0
        for co in c:
            
            b=co.total_cost+b
        

        return render(request,'cart.html',{'ele':c,'elr':b})
@csrf_exempt
def cart1(request):

    if request.method=='POST':  
        data = request.POST["detail"]
        data=data[1:]
        obj=DETAIL.objects.get(product_name=data)
        cart=Cart.objects.get(product_id =data,userid = request.user.username,unique=0)
        if cart.quantity > 1:
            cart.quantity=cart.quantity-1
            cart.save()
            cart.total_cost=(cart.quantity)*(obj.price)
            cart.save()
            print(cart.total_cost)

            context={'ele':'ok'}

        else :
            cart.quantity=cart.quantity-1
            cart.delete()
            context={'ele':'ok'}
            
            

        
        return JsonResponse(context)
    else:
        c=Cart.objects.filter(userid=request.user.username,unique=0)
        
        return render(request,'cart.html',{'ele':c})
@csrf_exempt
def cart2(request):

    if request.method=='POST':  
        data = request.POST["detail"]
        data=data[1:]
        obj=DETAIL.objects.get(product_name=data)
        cart=Cart.objects.get(product_id =data,userid=request.user.username,unique=0)
        
        cart.quantity=cart.quantity+1
        cart.save()
        cart.total_cost=(cart.quantity)*(obj.price)
        cart.save()
        print(cart.total_cost)

        context={'ele':'ok'}
        return JsonResponse(context)
    else:
        c=Cart.objects.filter(userid=request.user.username,unique=0)
        
        return render(request,'cart.html',{'ele':c})
@csrf_exempt
def cart3(request):

    if request.method=='POST':  
        cart=Cart.objects.filter(userid=request.user.username,unique=0)
        
        for carts in cart:
            carts.unique=1
            carts.save()
    context={'op':'po'}
        
    return JsonResponse(context)
@csrf_exempt
def orders(request):

      
    cart=Cart.objects.filter(userid=request.user.username,unique=1)  
    return render(request,'orders.html',{'ele':cart})       
@csrf_exempt
def about(request):
    return render(request,"about.html")
    
     







  
