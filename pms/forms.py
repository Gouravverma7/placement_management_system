from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser,StudentProfile, CompanyProfile

class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'role','phone_number']



class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['name', 'contact_info', 'skills', ]

class CompanyProfileForm(forms.ModelForm):
    class Meta:
        model = CompanyProfile
        fields = ['company_name', 'description', 'industry',]