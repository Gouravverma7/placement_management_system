from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    ##
    path('logout/', auth_views.LogoutView.as_view(template_name='pms/logout.html'), name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
    
    ##
    path('',views.home,name='home'),
    path('student_dashboard',views.student_dashboard,name='student_dashboard'),
    path('company_dashboard',views.company_dashboard,name='company_dashboard'),
    # path('job_postings/', views.job_postings, name='job_postings'),
    path('registration/', views.registration, name='registration'),
    path('login/', views.user_login, name='user_login'),
    path('student/profile/',views.view_student_profile, name='view_student_profile'),
    path('student/edit_profile/',views.edit_student_profile, name='edit_student_profile'),
    path('company/profile/',views.view_company_profile,name='view_company_profile'),
    path('company/edit_profile/',views.edit_company_profile, name='edit_company_profile'),
    path('job-listing/', views.job_listing, name='job_listing'),
    path('apply-for-job/<int:job_id>/', views.apply_for_job, name='apply_for_job'),
    path('post-job/', views.post_job, name='post_job'),
    path('posted-jobs',views.company_job_postings,name='posted_jobs'),
    path('edit-job/<int:job_id>/', views.edit_job_posting, name='edit_job_posting'),
    path('job-applications/', views.job_applications, name='job_applications'),
    path('accept-application/<int:application_id>/', views.accept_application, name='accept_application'),
    path('reject-application/<int:application_id>/', views.reject_application, name='reject_application'),
    path('applied-jobs/', views.applied_jobs, name='applied_jobs'),
    
    
]