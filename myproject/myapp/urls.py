from turtle import home
from django.urls import path,include
from . import views
from django.contrib import admin 
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.conf.urls import url
urlpatterns =[
    path('register/',views.register,name="register"),
    path('login/',views.login,name="login"),
    path('',views.index,name="index"),
    path('logout/',views.logout,name="logout"),
    path('electronics/',views.electronics,name="electronics"),
    path('grocery/',views.grocery,name="grocery"),
    path('eatable/',views.eatable,name="eatable"),
    path('clothes/',views.clothes,name="clothes"),
    path('cart/',views.cart,name="cart"),
    path('cart1/',views.cart1,name="cart1"),
    path('cart2/',views.cart2,name="cart2"),
    path('cart3/',views.cart3,name="cart3"),
    path('orders/',views.orders,name="orders"),
    path('about/',views.about,name="about"),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]