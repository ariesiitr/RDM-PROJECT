from turtle import home
from django.urls import path
from . import views
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
]