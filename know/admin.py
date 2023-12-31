from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Contact)
class AdminContact(admin.ModelAdmin):
    list_display = ['name','email','subject','message']


@admin.register(Person)
class AdminPerson(admin.ModelAdmin):
    list_display =['firstname','image']


@admin.register(Address)
class AdminAddress(admin.ModelAdmin):
    list_display=[]

@admin.register(Income)
class AdminIncome(admin.ModelAdmin):
    list_display=[]

@admin.register(Family)
class AdminFamily(admin.ModelAdmin):
    list_display=[]

