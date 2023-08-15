from django.shortcuts import render
from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.contrib import messages
from .forms import ContactForm,PersonForm,AddressForm,IncomeForm,FamilyForm
from django.conf import settings
from django.core.mail import send_mail
import smtplib
from django.forms import formset_factory
from .serializers import AddressSerializer, IncomeSerializer, FamilySerializer, PersonSerializer
from rest_framework import viewsets,generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
def index(request):
    return render(request,'pages/index.html')

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
        print('here')
        print(form)

        if (
            form.is_valid() and
            address_form.is_valid() and
            income_form.is_valid() and
            family_form.is_valid()
        ):
            person = form.save()
            # address = address_form.save(commit=False)
            income = income_form.save(commit=False)
            family = family_form.save(commit=False)
            # address.person = person
            income.person = person
            family.person = person
            # Associate the related Person instance with the other models
            address_option = request.POST.get('addressOption')
            if address_option =='yes':
                permanent_address = address_form.save(commit=False)
                permanent_address.person = person
                permanent_address.address_type = 'both'
                permanent_address.save()


               
            elif address_option == 'no':
                # Save permanent and temporary addresses
                permanent_address = address_form.save(commit=False)
                permanent_address.person = person
                permanent_address.address_type = 'permanent'
                permanent_address.save()

                # temporary_address = address_form.save(commit=False)
                # temporary_address.person = person
                # temporary_address.address_type = 'temporary'
                # temporary_address.save()
             
            # address.save()
            income.save()
            family.save()
            messages.success(request,"Data Added Successfully")
            return redirect('kyc')
        else:
            # Print form errors to the console
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
# def kyc(request):
#     form = PersonForm()
#     if request.method=="POST":
#         form = PersonForm(request.POST,request.FILES)
        
#         print('here')
#         print(form)
#         if form.is_valid():
#             # instance = form.save(commit=False)
#             # instance.image = 'photos/images' + instance.image.name
#             # instance.front_photo = 'citizen/front' + instance.front_photo.name
#             # instance.back_photo = 'citizen/back' + instance.back_photo.name
            
#             form.save()
          
#             return redirect('address')
#         else:
#             print('Form error:',form.errors)
#     else:
#         form =PersonForm()

#     return render(request,'pages/kyc3.html',{'form':form})
# def kyc1(request):
#     form1 = AddressForm()
#     if request.method=="POST":
#         form1 = AddressForm(request.POST,request.FILES)
#         if form1.is_valid():
#             form1.save()
#             return redirect('index')
#         else:
#              print('Form error:',form1.errors)
#     else:
#         form1 = AddressForm()
#     return render(request,'pages/kyc3.html',{'form1':form1})
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

class PersonViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

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