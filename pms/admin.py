from django.contrib import admin
from .models import CustomUser,StudentProfile,CompanyProfile
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(StudentProfile)
admin.site.register(CompanyProfile)