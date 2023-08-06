from django.shortcuts import render
from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.contrib import messages
from .forms import ContactForm,PersonForm,AddressForm,IncomeForm,FamilyForm
from django.conf import settings
from django.core.mail import send_mail
import smtplib
from django.forms import formset_factory


# Create your views here.
def index(request):
    return render(request,'pages/index.html')

def kyc(request):
    if request.method == 'POST':
        form = PersonForm(request.POST, request.FILES)
        if form.is_valid():
            person = form.save()

            address_form = AddressForm(request.POST)
            if address_form.is_valid():
                address = address_form.save(commit=False)
                address.user = person.user
                address.save()
                        
                return render(request, 'pages/kyc3.html', {'address_form':address_form})
                family_form = FamilyForm(request.POST)
                if family_form.is_valid():
                    family = family_form.save(commit=False)
                    family.person = person
                    family.save()

                    income_form = IncomeForm(request.POST)
                    if income_form.is_valid():
                        income = income_form.save(commit=False)
                        income.person = person
                        income.save()
                        # Now all the data for person, address, family, and income are saved
                        # You can now send this data to the API if required.
                        return redirect('kyc')
    else:
        person_form = PersonForm()
      
        
    return render(request, 'pages/kyc3.html', {'form': person_form})

# def kyc(request):

#     return render(request,'pages/kyc3.html')

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