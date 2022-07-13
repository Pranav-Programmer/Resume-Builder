from django.contrib import admin
from django.urls import path,include
from cred import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.loginUser,name='login'),
    path('logout',views.logoutUser,name='logout'),
    path('Basetemplate',views.template,name='template'),
    path('sec1',views.sec1,name='sec1'),
    path('sec2',views.sec2,name='sec2'),
    path('sec3',views.sec3,name='sec3'),
    path('Beta')
]
