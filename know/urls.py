from django.urls import path,include
from . import views
from know.controller import authview
from rest_framework.routers import DefaultRouter
from .views import AddressViewSet, IncomeViewSet, FamilyViewSet, PersonViewSet,BankViewSet,CustomAuthToken

router = DefaultRouter()
router.register(r'addresses', AddressViewSet)
router.register(r'incomes', IncomeViewSet)
router.register(r'families', FamilyViewSet)
router.register(r'persons', PersonViewSet)
router.register(r'banks',BankViewSet )

urlpatterns = [
    path('',views.index,name='index'),
    
   
    path('contact',views.contact,name = 'contact'),
    path('about/',views.about,name="about"),
    path('register/',authview.register, name = 'register'),
    path('login/',authview.loginpage, name = 'loginpage'),
    path('logout/',authview.logoutpage, name ='logout'),
    path('api/', include(router.urls)),
    path('api/token/auth/',CustomAuthToken.as_view()),
    # path('kyc/#tab2/<int:id>',views.kyc1,name='address'),
    path('kyc/',views.kyc,name='kyc'),

    #Admin
    path('superadmin_login/', views.superadmin_login, name='superadmin_login'),
    path('superadmin_logout/', views.superadmin_logout, name='superadmin_logout'), 
    path('kycadmin/',views.kycadmin,name='kycadmin'),
    path('adminkyc/',views.adminkyc, name='adminkyc'),
    path('adminview/<int:pk>',views.adminview, name ='adminview'),
    path('kyc_delete/<int:id>',views.kyc_delete,name='kyc_delete'),
    path('update_kyc/<int:pk>',views.update_kyc,name='update_kyc'),
    path('notification/<int:pk>/', views.notification, name='notification'),
    path('verifiedkyc/',views.verifiedkyc,name='verifiedkyc'),
    path('createuser/', views.createuser, name='createuser'),
    path('totaluser/',views.totaluser,name='totaluser'),
    path('user_delete/<int:id>',views.user_delete,name='user_delete'),
    path('user_update/<int:id>',views.user_update,name='user_update'),
    path('download/', views.download_file, name='download_file'),
    path('verified_download/',views.verified,name='verified'),
    path('user_download/',views.userdownload,name='userdownload'),
  

]
