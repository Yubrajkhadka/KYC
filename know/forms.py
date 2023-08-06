from django.contrib.auth.forms import UserCreationForm
from .models import User,Contact,Person,Address,Income,Family,GENDER_STATUS,MARRIED_STATUS,NATIONALITY
from django import forms
from django.core.validators import RegexValidator
from django.core.validators import  MinLengthValidator,EmailValidator
from captcha.fields import CaptchaField


class CustomUserForm(UserCreationForm):
    username = forms.CharField(widget = forms.TextInput(attrs= {'class':'form-control my-2','placeholder':'Enter username'}))
    firstname = forms.CharField(widget = forms.TextInput(attrs= {'class':'form-control my-2','placeholder':'Enter firstname'}), validators=[
            RegexValidator(
                regex=r'^[a-zA-Z]+$',
                message='First name must contain only alphabet letters.',
                code='invalid_first_name'
            )])
    lastname = forms.CharField(widget = forms.TextInput(attrs= {'class':'form-control my-2','placeholder':'Enter lastname'}),validators=[
            RegexValidator(
                regex=r'^[a-zA-Z]+$',
                message='Last name must contain only alphabet letters.',
                code='invalid_first_name'
            )])
    email = forms.CharField(widget = forms.EmailInput(attrs= {'class':'form-control my-2','placeholder':'Enter email'}),  validators=[
        EmailValidator(message='Enter a valid email address.'),])
    password1 = forms.CharField(widget = forms.PasswordInput(attrs= {'class': 'form-control my-2',
            'placeholder': 'Enter Password ',
            'title': 'Password must be at least 8 characters long and contain at least one uppercase letter, one digit, and one special character.'}), 
                                                                      
         validators=[
            MinLengthValidator(8, message='Password must be at least 8 characters long.'),
            RegexValidator(
                regex=r'^(?=.*[A-Z])(?=.*\d)(?=.*[\W_])[A-Za-z\d\W_]{8,}$',
                message='Password must contain at least one uppercase letter, one digit, and one special character.',
                code='invalid_password'
            )
        ])
    password2 = forms.CharField(widget = forms.PasswordInput(attrs= {'class':'form-control my-2','placeholder':'Confirm password','title':'Reenter Password'}),  validators=[
            RegexValidator(
                regex=r'^(?=.*[A-Z])(?=.*\d)(?=.*[\W_])[A-Za-z\d\W_]{8,}$',
                message='Password must contain at least one uppercase letter, one digit, and one special character.',
                code='invalid_password'
            )
        ])
   


    class Meta:
        model = User
        fields = ['username','firstname','lastname','email','password1','password2']



class ContactForm(forms.Form):
    fullname = forms.CharField(widget = forms.TextInput(attrs= {'class':'form-control my-2','placeholder':'Enter Full Name'}))
    email = forms.CharField(widget = forms.EmailInput(attrs= {'class':'form-control my-2','placeholder':'Enter Email','style': 'text-transform: lowercase;'}))
    number = forms.CharField(widget = forms.NumberInput(attrs= {'class':'form-control my-2','placeholder':'Enter Contact Number'}))
    subject = forms.CharField(widget = forms.TextInput(attrs= {'class':'form-control my-2','placeholder':'Enter Subject'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control my-2', 'placeholder': 'Enter Message'}))
    captcha = CaptchaField()
    class Meta:
        model = Contact
        fields = ['fullname','email','subject','message']


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
        widgets = {
            'firstname':forms.TextInput(attrs={'class':'form-control'}),
            'middlename':forms.TextInput(attrs={'class':'form-control'}),
            'lastname':forms.TextInput(attrs={'class':'form-control'}),
            'image':forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'fathername':forms.TextInput(attrs={'class':'form-control'}),
            'grandfathername':forms.TextInput(attrs={'class':'form-control'}),
            'dateofbirth':forms.DateInput(attrs={'class':'form-control','type': 'date'}),
            'gender':forms.Select(attrs={'class': 'form-control'}),
            'married_status':forms.Select(attrs={'class': 'form-control'}),
            'pannum':forms.TextInput(attrs={'class':'form-control'}),
            'nationality':forms.Select(attrs={'class': 'form-control'}),
            'citizenshipnumber':forms.TextInput(attrs={'class':'form-control'}),
            'citizen_issued_district':forms.TextInput(attrs={'class':'form-control'}),
            'citizen_issued_date':forms.DateInput(attrs={'class':'form-control','type': 'date'}),
            'front_photo':forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'back_photo':forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'passport_number':forms.TextInput(attrs={'class':'form-control'}),
            'passport_issued_date':forms.DateInput(attrs={'class':'form-control','type': 'date'}),
            'passport_issued_place':forms.TextInput(attrs={'class':'form-control'}),
            'pass_front_photo':forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'pass_back_photo':forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'other_card':forms.TextInput(attrs={'class':'form-control'}),
            'other_card_number':forms.TextInput(attrs={'class':'form-control'}),
            'other_card_issued_date':forms.DateInput(attrs={'class':'form-control','type': 'date'}),
            'other_card_issued_authority':forms.TextInput(attrs={'class':'form-control'}),
            'other_card_front':forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'other_card_back':forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'number':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            }
        
class AddressForm(forms.ModelForm):
    class Meta:
        Model = Address
        fields = '__all__'
        widgets ={
            'zone' : forms.TextInput(attrs={'class':'form-control'}),
            'provience':forms.TextInput(attrs={'class':'form-control'}),
            'district':forms.TextInput(attrs={'class':'form-control'}),
            'muni_vdc':forms.TextInput(attrs={'class':'form-control'}),
            'house_no':forms.TextInput(attrs={'class':'form-control'}),
            'ward_no':forms.TextInput(attrs={'class':'form-control'}),
            'street':forms.TextInput(attrs={'class':'form-control'}),
            'tel_n0':forms.TextInput(attrs={'class':'form-control'}),
            'post_box':forms.TextInput(attrs={'class':'form-control'}),
            'l_image':forms.TextInput(attrs={'class':'form-control'}),
            }

class IncomeForm(forms.ModelForm):
    class Meta:
        Model = Income
        fields = '__all__'

class FamilyForm(forms.ModelForm):
    class Meta:
        model = Family 
        fields ='__all__'

    


