from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from .forms import StudentProfileForm
from .models import Student
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm
from django.contrib.auth.decorators import login_required
from .models import Attendance

# Create your views here.
@login_required
def attendance_view(request):
    attendance = Attendance.objects.filter(user=request.user)
    context = {
        'attendance': attendance
    }
    return render(request, 'attendance/view.html', context)
def student_dashboard(request):
    student = Student.objects.get(user=request.user)
    context = {
        'student': student
    }
    return render(request, 'student/dashboard.html', context)
def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserLoginForm()
    return render(request, 'registration/login.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


def welcome_page(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')
@login_required
def student_view(request):
    student = request.user.student  # Retrieve the student instance for the logged-in student
    
    if request.method == 'POST':
        form = StudentProfileForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the profile page after successful update
    else:
        form = StudentProfileForm(instance=student)
        
    context = {
        'student': student,
        'form': form,
    }
    return render(request, 'student/view.html', context)