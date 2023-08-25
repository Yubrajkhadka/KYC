from django.shortcuts import render
import csv
from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.contrib import messages
from .forms import ContactForm,PersonForm,AddressForm,IncomeForm,FamilyForm,CustomUserForm
from django.conf import settings
from django.core.mail import send_mail
import smtplib
from django.core.paginator import Paginator, Page
from django.forms import formset_factory
from .serializers import AddressSerializer, IncomeSerializer, FamilySerializer, PersonSerializer,BankSerializer
from rest_framework import viewsets,generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from twilio.rest import Client
from django.http import HttpResponse  # Import HttpResponse
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.http import FileResponse




# Create your views here.
def index(request):
   
    return render(request, 'pages/index.html')

def about(request):
    return render(request,'pages/about.html')

@login_required(login_url ='loginpage')
def kyc(request):
    global form, address_form, income_form, family_form
    address_form = AddressForm()
    form = PersonForm(prefix='person')
    income_form = IncomeForm(prefix='income')
    family_form = FamilyForm(prefix='family')
    
    if request.method == 'POST':
        form = PersonForm(request.POST, request.FILES, prefix='person')
        address_form = AddressForm(request.POST,request.FILES, prefix='address')
        income_form = IncomeForm(request.POST, prefix='income')
        family_form = FamilyForm(request.POST, prefix='family')
        
        if (
            form.is_valid() and
            address_form.is_valid() and
            income_form.is_valid() and
            family_form.is_valid()
        ):
            person = form.save()  # Save the person data

            address = address_form.save(commit=False)
            address.person = person  # Associate the address with the person
            address.save()

            income = income_form.save(commit=False)
            income.person = person  # Associate the income with the person
            income.save()

            family = family_form.save(commit=False)
            family.person = person  # Associate the family with the person
            family.save()
            # Sending SMS notification
           
            try:
                client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
                to_phone_number =  "+977" + form.cleaned_data['number']   # Replace with the recipient's phone number
                message_body = "KYC data has been successfully saved!"
                client.messages.create(
                    to=to_phone_number,
                    from_=settings.TWILIO_PHONE_NUMBER,
                    body=message_body
                )
                print("SMS notification sent successfully")
                messages.success(request, "Data Added Successfully")
                return redirect('kyc')
            except Exception as e:
                print("Error sending SMS:", str(e))
                messages.error(request, "Form data has errors. Please check the fields.")
        
        else:
            messages.error(request, "Form data has errors. Please check the fields.")
            print('Form errors:', form.errors)
            print('Address Form errors:', address_form.errors)
            print('Income Form errors:', income_form.errors)
            print('Family Form errors:', family_form.errors)
    else:
        form = PersonForm(prefix='person')
        address_form = AddressForm(prefix='address')
        income_form = IncomeForm(prefix='income')
        family_form = FamilyForm(prefix='family')

    return render(
        request,
        'pages/kyc3.html',
        {
            'form': form,
            'form1': address_form,
            'form2': income_form,
            'form3': family_form,
        }
    )

def contact(request):
    form = ContactForm()
    if request.method == "POST":
       form = ContactForm(request.POST)
       if form.is_valid():
            name = request.POST.get('fullname')
            email = request.POST.get('email')
            number = request.POST.get('number')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            contact = Contact(
                name = name,
                email = email,
                number = number,
                subject = subject,
                message = message,
                )
            subject = subject
            message = message
            email_from = settings.EMAIL_HOST_USER
            try:
                send_mail(subject, message ,email_from,['yubrajkhadka@kcc.edu.np'])
                contact.save()
                messages.success(request,"Message sent successfully")
                return redirect('/')
            except smtplib.SMTPException as e:
                  messages.error(request, f"Message could not be sent. Error: {e}")
                  return redirect('/contact')
       else:
            messages.error(request, 'Wrong Captcha!')
    context = {'form':form}      
    return render(request, 'pages/contact.html',context)  



#admin

def superadmin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('kycadmin')  # Redirect to admin dashboard
        else:
            error_message = "Invalid credentials or not a superuser."
            # messages.error(request, error_message)
    return render(request, 'admin/pages/login.html')
    
def superadmin_logout(request):
    logout(request)
    return redirect('superadmin_login')

@login_required(login_url='superadmin_login') 
def kycadmin(request):
    person =Person.objects.all()
    verify_kyc = Person.objects.filter(verified=True)
    unverify =Person.objects.filter(verified=False)
    total_person = person.count()
    total_verifiedperson =verify_kyc.count()
    total_unverify = unverify.count()
    total_users = User.objects.count()
    context ={
        'total_person':total_person,
        'total_verifiedperson':total_verifiedperson,
        'total_unverify': total_unverify,
        'total_user':total_users
    }
    return render(request,'admin/pages/index.html',context)
def adminkyc(request):
    kyc = Person.objects.filter(verified=False)
    items_per_page = 5
    paginator = Paginator(kyc, items_per_page)
    page_number = request.GET.get('page')
    page_obj: Page = paginator.get_page(page_number)    
 
    data = {
        'person':page_obj
    }
    return render(request,'admin/pages/kyc.html',data)
  

def adminview(request,pk):
    person = get_object_or_404(Person, pk=pk)
    income = person.income.all()
    address = person.addresses.all()
    family = person.family.all()
    data = {
        'person':person,
        'a':address,
        'i':income,
        'f':family,
    }
    return render(request,'admin/pages/kycview.html',data)

def kyc_delete(request,id):
     person = get_object_or_404(Person, id=id)
     person.delete() 
     messages.success(request,'Data has been Deleted Successfully.')
     redirect_back = request.META.get('HTTP_REFERER')
     return redirect(redirect_back)

def notification(request,pk):
    try:
        if request.method == 'POST':
            print('here')
            kyc_data = Person.objects.get(pk=pk)
            kyc_data.verified = True
            kyc_data.save()
            client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
            to_phone_number = '+9779861562381'
            message_body = "KYC data has been Verified!"
            client.messages.create(
                to=to_phone_number,
                from_=settings.TWILIO_PHONE_NUMBER,
                body=message_body
            )
            messages.success(request, "Data Verified Successfully")
            return redirect('kycadmin')  # Redirect to the desired URL after successful verification

        else:
            redirect_back = request.META.get('HTTP_REFERER')
            return redirect(redirect_back)
    except Exception as e:
        print("Error sending SMS:", str(e))
        return HttpResponse("Error sending SMS")
    

def update_kyc(request, pk):
    person = get_object_or_404(Person, pk=pk)
    
    if request.method == 'POST':
        form = PersonForm(request.POST, request.FILES, instance=person)
        form1 = AddressForm(request.POST,request.FILES, instance=person.addresses.first())
        form2 = IncomeForm(request.POST, instance=person.income.first())
        form3 = FamilyForm(request.POST, instance=person.family.first())
        
        if form.is_valid() and form1.is_valid() and form2.is_valid() and form3.is_valid():
            form.save()
            form1.save()
            form2.save()
            form3.save()
            
            messages.success(request, "KYC Updated Successfully")
            return redirect('adminkyc')
    else:
        form = PersonForm(instance=person)
        address_instance = person.addresses.first()
        income_instance = person.income.first()
        family_instance = person.family.first()
        
        form1 = AddressForm(instance=address_instance) if address_instance else AddressForm()
        form2 = IncomeForm(instance=income_instance) if income_instance else IncomeForm()
        form3 = FamilyForm(instance=family_instance) if family_instance else FamilyForm()
        
    return render(request, 'admin/pages/updatekyc.html', {
        'form': form,
        'form1': form1,
        'form2': form2,
        'form3': form3,
        'person': person,
    })



def download_file(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="person_information.csv"'

    writer = csv.writer(response)

    # Get all the field names from the models' _meta attribute
    person_fields = [field.name for field in Person._meta.get_fields() if field.concrete]
    address_fields = [field.name for field in Address._meta.get_fields() if field.concrete]
    income_fields = [field.name for field in Income._meta.get_fields() if field.concrete]
    family_fields = [field.name for field in Family._meta.get_fields() if field.concrete]

    all_fields = person_fields + address_fields + income_fields + family_fields
   

    writer.writerow(all_fields )  # Write the header row

    persons = Person.objects.all()

    for person in persons:
        person_data = [getattr(person, field) for field in person_fields]
        addresses = person.addresses.all()
        incomes = person.income.all()
        families = person.family.all()

        for address in addresses:
            address_data = [getattr(address, field) for field in address_fields]
            for income in incomes:
                income_data = [getattr(income, field) for field in income_fields]
                for family in families:
                    family_data = [getattr(family, field) for field in family_fields]

                    # Combine all data and write to CSV row
                    row = person_data + address_data + income_data + family_data
                    writer.writerow(row)

    return response

def verified(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="verified_kyc_data.csv"'

    writer = csv.writer(response)

    person_fields = [field.name for field in Person._meta.get_fields() if field.concrete]
    address_fields = [field.name for field in Address._meta.get_fields() if field.concrete]
    income_fields = [field.name for field in Income._meta.get_fields() if field.concrete]
    family_fields = [field.name for field in Family._meta.get_fields() if field.concrete]

    all_fields = person_fields + address_fields + income_fields + family_fields
    writer.writerow(all_fields)

    verified_persons = Person.objects.filter(verified=True)

    for person in verified_persons:
        person_data = [getattr(person, field) for field in person_fields]

        addresses = Address.objects.filter(person=person)
        incomes = Income.objects.filter(person=person)
        families = Family.objects.filter(person=person)

        for address in addresses:
            address_data = [getattr(address, field) for field in address_fields]
            for income in incomes:
                income_data = [getattr(income, field) for field in income_fields]
                for family in families:
                    family_data = [getattr(family, field) for field in family_fields]

                    row = person_data + address_data + income_data + family_data
                    writer.writerow(row)

    return response


def userdownload(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="User_Data.csv"'

    writer = csv.writer(response)

    user_fields = [field.name for field in User._meta.get_fields() if field.concrete]

    all_fields = user_fields 
    writer.writerow(all_fields)

    users = User.objects.all()

    for user in users:
        user_data = [getattr(user, field) for field in user_fields]
        writer.writerow(user_data)

    return response



def verifiedkyc(request):
    kyc_list = Person.objects.filter(verified=True)
    
    # Number of items per page
    items_per_page = 5  # Adjust this number as needed
    
    paginator = Paginator(kyc_list, items_per_page)
    
    page_number = request.GET.get('page')
    page_obj: Page = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj
    }
    
    return render(request, 'admin/pages/verifiedkyc.html', context)

def createuser(request):
    form = CustomUserForm()
   
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
       
        if form.is_valid() :
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            email = form.cleaned_data['email']
            user = User.objects.create_user(username=username,email=email,password=password,first_name=firstname,last_name=lastname)
            user.first_name = firstname
            user.last_name = lastname
            user.save()
            messages.success(request,"User Create  Successfully")
            return redirect('kycadmin')
    context = {'form':form}
    return render(request,"admin/pages/createuser.html",context)

def totaluser(request):
    user = User.objects.all()
    items_per_page = 4
    paginator = Paginator(user, items_per_page)
    page_number = request.GET.get('page')
    page_obj: Page = paginator.get_page(page_number)
    data= {
        'user':page_obj
    }
    return render(request,'admin/pages/user.html',data)

def total_message(request):
    contact = Contact.objects.all()
    items_per_page = 4
    paginator = Paginator(contact, items_per_page)
    page_number = request.GET.get('page')
    page_obj: Page = paginator.get_page(page_number)
    data= {
        'contact':page_obj
    }
    return render(request,'admin/pages/contact.html',data)
def delete_contact(request,id):
     contact = get_object_or_404(Contact, id=id)
     contact.delete() 
     messages.success(request,'Data has been Deleted Successfully.')
     redirect_back = request.META.get('HTTP_REFERER')
     return redirect(redirect_back)

def user_delete(request,id):
     user = get_object_or_404(User, id=id)
     user.delete() 
     messages.success(request,'Data has been Deleted Successfully.')
     redirect_back = request.META.get('HTTP_REFERER')
     return redirect(redirect_back)

def user_update(request,id):
    user = get_object_or_404(User, pk=id)
    if request.method=="POST":
      form =  CustomUserForm(request.POST, request.FILES, instance=user)
      if form.is_valid():
          form.save()
          messages.success(request, "KYC Updated Successfully")
          return redirect('totaluser')
      else:
          form= CustomUserForm()
    data ={
         'user':user  
       }
    return render(request,"admin/pages/user.html",data)



#API
class AddressViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class IncomeViewSet(viewsets.ModelViewSet):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer

class FamilyViewSet(viewsets.ModelViewSet):
    queryset = Family.objects.all()
    serializer_class = FamilySerializer

# class PersonList(generics.ListCreateAPIView):
#     queryset = Person.objects.all()
#     serializer_class = PersonSerializer

# class PersonViewSet(viewsets.ModelViewSet):
#     queryset = Person.objects.all()
#     serializer_class = PersonSerializer

# class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Person.objects.all()
#     serializer_class = PersonSerializer
class BankViewSet(viewsets.ModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    @action(detail=False, methods=['post'])
    def create_no_slash(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)  
        return Response(serializer.errors, status=400)  



class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.id,
            'email': user.email,
        })
    
class PersonViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
   # Enforce authentication for these views
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        address_serializer = AddressSerializer(instance.addresses.all(), many=True)
        income_serializer = IncomeSerializer(instance.income.all(), many=True)
        family_serializer = FamilySerializer(instance.family.all(), many=True)

        data = {
            'person': self.serializer_class(instance).data,
            'addresses': address_serializer.data,
            'income': income_serializer.data,
            'family': family_serializer.data,
        }

        return Response(data)

    def create(self, request, *args, **kwargs):
        return Response({"detail": "Creating new person is not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self, request, *args, **kwargs):
        return Response({"detail": "Updating person details is not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def partial_update(self, request, *args, **kwargs):
        return Response({"detail": "Partial updates are not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def destroy(self, request, *args, **kwargs):
        return Response({"detail": "Deleting a person is not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)