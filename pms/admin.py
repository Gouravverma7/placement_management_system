from django.contrib import admin
from .models import CustomUser,StudentProfile,CompanyProfile,JobPosting,JobApplication
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(StudentProfile)
admin.site.register(CompanyProfile)
admin.site.register(JobApplication)
admin.site.register(JobPosting)