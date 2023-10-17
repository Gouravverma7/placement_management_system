from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegistrationForm,StudentProfileForm,CompanyProfileForm,JobPostingForm,JobApplicationForm
from .models import StudentProfile,CompanyProfile,JobPosting,JobApplication

def home(request):
    return render(request,'pms/home.html')

def student_dashboard(request):
    return render(request,'pms/student_dashboard.html')

def company_dashboard(request):
    return render(request,'pms/company_dashboard.html')

def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            if user.is_student():
                student_profile = StudentProfile(user=user)
                student_profile.save()
            elif user.is_company():
                company_profile = CompanyProfile(user=user)
                company_profile.save()
            
            login(request, user)
            if user.is_student():
                # Redirect to the student dashboard or another view
                return redirect('index')
            elif user.is_company():
                # Redirect to the company dashboard or another view
                return redirect('index1')
    else:
        form = RegistrationForm()
    return render(request, 'pms/registration.html', {'form': form})



def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_student():
                # Redirect to the student dashboard or another view
                return redirect('student_dashboard')
            elif user.is_company():
                # Redirect to the company dashboard or another view
                return redirect('company_dashboard')
            else:
                # Debug statement to print the user's role
                print("User has an unknown role")
        else:
            messages.error(request, 'Invalid login credentials. Please try again.')
    return render(request, 'pms/login.html', {'messages': messages.get_messages(request)})

#view for student profile 
@login_required
def view_student_profile(request):
    # Retrieve the student's profile
    print(request.user.role)

    student_profile = StudentProfile.objects.get(user=request.user)
    return render(request, 'pms/student_profile.html', {'student_profile': student_profile})

#view for editing student profile 
@login_required
def edit_student_profile(request):
    student_profile = StudentProfile.objects.get(user=request.user)

    if request.method == 'POST':
        form = StudentProfileForm(request.POST, instance=student_profile)
        if form.is_valid():
            form.save()
            return redirect('view_student_profile')
    else:
        form = StudentProfileForm(instance=student_profile)

    return render(request, 'pms/edit_student_profile.html', {'form': form})


#view for company profiles
@login_required
def view_company_profile(request):
    # Retrieve the student's profile
    print(request.user)

    company_profile = CompanyProfile.objects.get(user=request.user)
    return render(request, 'pms/company_profile.html', {'company_profile': company_profile})

#view for editing company profile 
@login_required
def edit_company_profile(request):
    company_profile = CompanyProfile.objects.get(user=request.user)

    if request.method == 'POST':
        form = CompanyProfileForm(request.POST, instance=company_profile)
        if form.is_valid():
            form.save()
            return redirect('view_company_profile')
    else:
        form = CompanyProfileForm(instance=company_profile)

    return render(request, 'pms/edit_company_profile.html', {'form': form})

#to post jobs 
@login_required
def post_job(request):
    if request.user.is_company():
        if request.method == 'POST':
            form = JobPostingForm(request.POST)
            if form.is_valid():
                job_posting = form.save(commit=False)
                job_posting.company = request.user.companyprofile  # Associate job posting with the company
                job_posting.save()
                return redirect('company_dashboard')  # Redirect to the job listing page
        else:
            form = JobPostingForm()
        return render(request, 'pms/job_posting_form.html', {'form': form})
    else:
        return render(request, 'pms/access_denied.html')  # Customize this template

#to apply for jobs
@login_required
def apply_for_job(request, job_id):
    job = JobPosting.objects.get(pk=job_id)

    if request.user.is_student:
        if request.method == 'POST':
            form = JobApplicationForm(request.POST)
            if form.is_valid():
                application = form.save(commit=False)
                application.job = job
                application.applicant = request.user.studentprofile  # Associate the application with the student
                application.save()
                return redirect('job_listing')  # Redirect to the job listing page
        else:
            form = JobApplicationForm()
        return render(request, 'pms/job_application_form.html', {'form': form, 'job': job})
    else:
        return render(request, 'pms/access_denied.html') 
    
    
#job listing view for students 
def job_listing(request):
    job_postings = JobPosting.objects.filter(is_active=True)  # Retrieve active job postings
    return render(request, 'pms/job_listing.html', {'job_postings': job_postings})

#job application view
def job_applications(request):
    # Retrieve job applications for the current company (assuming the user is a company)
    if request.user.is_company:
        job_applications = JobApplication.objects.filter(job__company=request.user.companyprofile)
        return render(request, 'pms/job_applications.html', {'job_applications': job_applications})
    else:
        return render(request, 'access_denied.html')  # Customize this template


def accept_application(request, application_id):
    application = get_object_or_404(JobApplication, pk=application_id)
    # Check if the user has permission to accept/reject this application (e.g., check if the user is the owner of the associated job posting)
    
    if request.method == 'POST':
        application.status = 'accepted'  # Update the application status to 'accepted'
        application.save()
        # You can also send a notification to the student about the acceptance.

    # Redirect back to the job applications management page or job posting details page.
    return redirect('job_applications')

def reject_application(request, application_id):
    application = get_object_or_404(JobApplication, pk=application_id)
    # Check if the user has permission to accept/reject this application (e.g., check if the user is the owner of the associated job posting)

    if request.method == 'POST':
        application.status = 'rejected'  # Update the application status to 'rejected'
        application.save()
        # You can also send a notification to the student about the rejection.

    # Redirect back to the job applications management page or job posting details page.
    return redirect('job_applications')

#applied jobs
def applied_jobs(request):
    if request.user.is_student:
        # Retrieve job applications related to the current student
        job_applications = JobApplication.objects.filter(applicant=request.user.studentprofile)
        return render(request, 'pms/applied_jobs.html', {'job_applications': job_applications})
    else:
        return render(request, 'pms/access_denied.html')