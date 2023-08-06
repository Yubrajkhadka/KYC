from django.urls import path
from . import views
from know.controller import authview

urlpatterns = [
    path('',views.index,name='index'),

    path('contact',views.contact,name = 'contact'),
    path('register/',authview.register, name = 'register'),
    path('login/',authview.loginpage, name = 'loginpage'),
    path('logout/',authview.logoutpage, name ='logout'),

    path('kyc/',views.kyc,name='kyc'),



]
