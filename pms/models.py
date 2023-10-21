from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('company', 'Company'),
    )
    
    email = models.EmailField(max_length=254)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    phone_number = models.CharField(max_length=10)
    
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
    profile_picture = models.ImageField(upload_to='student_profile_pics/', null=True, blank=True)

    
    def __str__(self):
        return self.name

class CompanyProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    # Add company-specific fields like 'company_name', 'description', 'industry', etc.
    company_name = models.CharField(max_length=100)
    description = models.TextField()
    industry = models.CharField(max_length=100)
    
    profile_picture = models.ImageField(upload_to='company_profile_pics/', null=True, blank=True)

    # Add other fields as needed
    def __str__(self):
        return self.company_name


class JobPosting(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    application_deadline = models.DateField()
    is_active = models.BooleanField(default=True)
    # Add other fields as needed

class JobApplication(models.Model):
    job = models.ForeignKey(JobPosting, on_delete=models.CASCADE)
    applicant = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    cover_letter = models.TextField()
    status = models.CharField(max_length=20, choices=[("pending", "Pending"), ("accepted", "Accepted"), ("rejected", "Rejected")], default="pending")
    application_date = models.DateTimeField(auto_now_add=True)
    # Add other fields as needed