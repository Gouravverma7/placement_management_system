from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser,StudentProfile, CompanyProfile,JobApplication,JobPosting

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Enter a valid email address.')
    phone_number = forms.CharField(max_length=20, required=True)
    role = forms.ChoiceField(choices=CustomUser.ROLE_CHOICES, required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone_number', 'role', 'password1', 'password2')



class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['name', 'contact_info', 'skills','profile_picture', ]

class CompanyProfileForm(forms.ModelForm):
    class Meta:
        model = CompanyProfile
        fields = ['company_name', 'description', 'industry','profile_picture',]
        
class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['cover_letter']

class JobPostingForm(forms.ModelForm):
    class Meta:
        model = JobPosting
        fields = ['title', 'description', 'application_deadline', 'is_active',]
