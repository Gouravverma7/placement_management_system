from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('student_dashboard',views.student_dashboard,name='student_dashboard'),
    path('company_dashboard',views.company_dashboard,name='student_dashboard'),
    # path('job_postings/', views.job_postings, name='job_postings'),
    path('registration/', views.registration, name='registration'),
    path('login/', views.user_login, name='user_login'),
    path('student/profile/',views.view_student_profile, name='view_student_profile'),
    path('student/edit_profile/',views.edit_student_profile, name='edit_student_profile'),
    path('company/profile/',views.view_company_profile,name='view_company_profile'),
    path('company/edit_profile/',views.edit_company_profile, name='edit_company_profile'),

    
    
]