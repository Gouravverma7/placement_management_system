from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegistrationForm,StudentProfileForm,CompanyProfileForm
from .models import StudentProfile,CompanyProfile

def index(request):
    return render(request,'pms/index.html')

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
                return redirect('index')
            elif user.is_company():
                # Redirect to the company dashboard or another view
                return redirect('index')
            else:
                # Debug statement to print the user's role
                print("User has an unknown role")
        else:
            messages.error(request, 'Invalid login credentials. Please try again.')
    return render(request, 'pms/login.html', {'messages': messages.get_messages(request)})


@login_required
def view_student_profile(request):
    # Retrieve the student's profile
    print(request.user.role)

    student_profile = StudentProfile.objects.get(user=request.user)
    return render(request, 'pms/student_profile.html', {'student_profile': student_profile})

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

# Similar views for company profiles
@login_required
def view_company_profile(request):
    # Retrieve the student's profile
    print(request.user)

    company_profile = CompanyProfile.objects.get(user=request.user)
    return render(request, 'pms/company_profile.html', {'company_profile': company_profile})

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