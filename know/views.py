from django.shortcuts import render
from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.contrib import messages
from .forms import ContactForm
from django.conf import settings
from django.core.mail import send_mail
import smtplib


# Create your views here.
def index(request):
    return render(request,'pages/index.html')

def kyc(request):
    return render(request,'pages/kyc.html')

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