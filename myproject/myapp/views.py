from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from numpy import product
from .models import DETAIL


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
    detail1=DETAIL.objects.all()

    response_data1 = {'created': 'YES',}

    return render(request,"electronics.html",{"detail1":detail1})
def eatable(request):
    response_data1 = {'created': 'YES',}
    return render(request,"eatable.html")
@csrf_exempt
def grocery(request):
    response_data1 = {'created': 'YES',}
    return render(request,"grocery.html")
@csrf_exempt
def clothes(request):
    response_data1 = {'created': 'YES',}
    return render(request,"clothes.html")
@csrf_exempt
def cart(request):

    if request.method=='POST':  
        data = request.POST["detail"]
        obj=DETAIL.objects.get(product_name=data)
        print(obj.price)
        context={'obj':obj,'created': 'YES'}
        return render(request,'cart.html',{'obj':obj})      
    else:
        return render(request,'cart.html')
    #     ALL = DETAIL.objects.all()
    #     contexqt={
    #         'ALL': ALL
    #     }
    #     return JsonResponse(contexqt) 
    # else:
    #     response_data1 = {'created': 'YES',}
    #     return render(request,"cart.html")   
