from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('company', 'Company'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    phone_number = models.CharField(max_length=50)

    # Add fields common to both students and companies
    

    def is_student(self):
        return self.role == 'student'

    def is_company(self):
        return self.role == 'company'
    


class StudentProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    # Add student-specific fields like 'name', 'contact_info', 'skills', etc.
    name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=100)
    skills = models.TextField()
    # Add other fields as needed
    
    def __str__(self):
        return self.name

class CompanyProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    # Add company-specific fields like 'company_name', 'description', 'industry', etc.
    company_name = models.CharField(max_length=100)
    description = models.TextField()
    industry = models.CharField(max_length=100)
    # Add other fields as needed
    def __str__(self):
        return self.company_name
