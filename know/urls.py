from django.urls import path,include
from . import views
from know.controller import authview
from rest_framework.routers import DefaultRouter
from .views import AddressViewSet, IncomeViewSet, FamilyViewSet, PersonViewSet

router = DefaultRouter()
router.register(r'addresses', AddressViewSet)
router.register(r'incomes', IncomeViewSet)
router.register(r'families', FamilyViewSet)
router.register(r'persons', PersonViewSet)

urlpatterns = [
    path('',views.index,name='index'),

    path('contact',views.contact,name = 'contact'),
    path('register/',authview.register, name = 'register'),
    path('login/',authview.loginpage, name = 'loginpage'),
    path('logout/',authview.logoutpage, name ='logout'),
    path('api/', include(router.urls)),
    # path('kyc/#tab2/<int:id>',views.kyc1,name='address'),
    path('kyc/',views.kyc,name='kyc'),
    

]
