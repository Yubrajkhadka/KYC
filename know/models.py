from django.db import models
from django.contrib.auth.models import User

from django.contrib.auth.models import AbstractUser

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class CustomUser(AbstractUser):
    contact = models.CharField(max_length = 10)
    image = models.ImageField(upload_to='photos/images')
    groups = None  
    user_permissions = None

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    number = models.CharField(default=False,max_length=10)
    message = models.TextField()
    def __str__(self):
        return self.name
    

MARRIED_STATUS = (
    ("Married", "Married"),
    ("UnMarried", "Unmarried"),
    ("Divorse", "Divorse"),
    ("Widow", "Widow"),
)

GENDER_STATUS =(
    ("Male","Male"),
    ("Female","Female"),
    ("Other","Other"),
)

NATIONALITY = (
    ("Nepalies","Nepalies"),
    ("Other","Other"),
)
    


class Person(models.Model):
    firstname = models.CharField(max_length=250)
    middlename = models.CharField(max_length=255,blank=True)
    lastname = models.CharField(max_length=255)
    image = models.ImageField(upload_to='photos/images')
    fathername = models.CharField(max_length=255)
    grandfather = models.CharField(max_length=255)
    dateofbirth = models.DateField()
    gender = models.CharField(max_length=50, choices=GENDER_STATUS, default="Male")
    married_status = models.CharField(max_length=50, choices=MARRIED_STATUS, default="UnMarried")
    pannum = models.CharField(max_length=20)
    nationality = models.CharField(max_length=50, choices=NATIONALITY, default="Nepalies")
    citizenshipnumber = models.CharField(max_length=50)
    citizen_issued_district = models.CharField(max_length=50)
    citizen_issued_date = models.DateField()
    front_photo = models.ImageField(upload_to='citizen/front')
    back_photo = models.ImageField(upload_to='citizen/back')
    passport_number = models.CharField(max_length=20)
    passport_issued_date = models.DateField()
    passport_issued_place = models.CharField(max_length=100)
    pass_front_photo = models.ImageField(upload_to='passport/front',blank=True)
    pass_back_photo = models.ImageField(upload_to='passport/back',blank=True)
    other_card = models.CharField(max_length=100,blank=True)
    other_card_number = models.CharField(max_length=20,blank=True)
    other_card_issued_date = models.DateField(blank=True)
    other_card_issued_authority = models.CharField(max_length=100,blank=True)
    other_card_front = models.ImageField(upload_to='other/front',default="",blank=True)
    other_card_back=models.ImageField(upload_to='other/back',default="",blank=True)
    email =models.CharField(max_length=25,default="")
    number = models.CharField(max_length=10,default="")
    verified = models.BooleanField(default=False)



class Address(models.Model):
    ADDRESS_TYPE_CHOICES = (
        ('permanent', 'Permanent'),
        ('temporary', 'Temporary'),
        ('both','Both')
    )
    Provience_CHOICES=(
        ('bagmati','Bagmati'),
        ('koshi','Koshi'),
        ('karnali','Karali'),
        ('madhesh','Madhesh'),
        ('ghandaki','Ghandaki'),
        ('lumbini','Lumbini'),
        ('sudherpachim','Sudherpachim')
    )
   
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='addresses')
    address_type = models.CharField(max_length=10, choices=ADDRESS_TYPE_CHOICES)
    zone = models.CharField(max_length=40)
    provience = models.CharField(max_length=50,choices=Provience_CHOICES)
    district = models.CharField(max_length=75)
    muni_vdc =models.CharField(max_length=75)
    house_no= models.CharField(max_length=10)
    ward_no= models.CharField(max_length=10)
    street= models.CharField(max_length=100)
    tel_n0 = models.CharField(max_length = 10, blank=True)
    post_box = models.CharField(max_length=20)
    l_image= models.ImageField(upload_to='location/image',default="")

    def __str__(self):
        return f"{self.address_type} Address for {self.person.firstname}"

class Income(models.Model):

   person= models.ForeignKey(Person, on_delete=models.CASCADE, related_name='income')
   organization = models.CharField(max_length=60)
   address = models.CharField(max_length = 100)
   designation  = models.CharField(max_length =20)
   def __str__(self):
        return f"Income details for {self.person.firstname}"
   

class Family(models.Model):
    
   person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='family')
   f_relation= models.CharField(max_length=100)
   f_fullname = models.CharField(max_length= 100)
   f_remarks = models.CharField(max_length=150)

   def __str__(self):
       return f"Family details for {self.person.firstname}"

class Bank(models.Model):
       person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='bank')
       account_no = models.CharField(max_length =20)
       Bank_name = models.CharField(max_length=10)
       address = models.CharField(max_length =20)
       created_at = models.DateTimeField(auto_now_add=True) 
       accounttype = models.CharField(max_length =15, default="Saving")