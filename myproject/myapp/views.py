from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

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