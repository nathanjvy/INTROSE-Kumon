from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.http import Http404
from django.views.generic import TemplateView
from django.shortcuts import redirect,reverse
from django.urls import reverse

# Create your views here.

from kumon.forms import LoginForm,StudentForm

from .models import User, Student

def login(request):
    form = LoginForm(request.POST)
    all_users = User.objects.all()

    if form.is_valid():
        lUser = form.cleaned_data['username']
        lPass = form.cleaned_data['password']

        for i in all_users:
            if i.username == lUser:
                if i.password == lPass:
                    print("LOGGED IN AYE")
                    return render(request, 'kumon/index.html', {'loggeduser': i})

    context = {
        'all_users': all_users,
        'form':form,
    }

    return render(request, 'kumon/login.html', context)	

def home(request):

    context = {
    }
    return render(request,'kumon/index.html',context)

def studentPage(request):
    all_students = Student.objects.all()
    context = {
        'all_students':all_students,
    }
    return render(request,'kumon/students.html',context)

def studentProfile(request, student_id):
    all_students = Student.objects.all()

    try:
        student = Student.objects.get(pk=student_id)
    except (KeyError, Student.DoesNotExist):
        raise Http404("User does not exist")


    context = {
        'all_students':all_students,
        'student':student,
    }
    return render(request,'kumon/student-profile.html',context)

def teacherPage(request):
    context = {}

    return render(request,'kumon/teachers.html',context)

def attendancePage(request):
    context = {}

    return render(request,'kumon/Attendance.html',context)

def schedulePage(request):
    context = {}

    return render(request,'kumon/Schedule.html',context)

def salaryPage(request):
    context = {}

    return render(request,'kumon/salaries.html',context)

def paymentPage(request):
    context = {}

    return render(request,'kumon/payment.html',context)

def expensesPage(request):
    context = {}

    return render(request,'kumon/expenses.html',context)

def inventoryPage(request):
    context = {
    }

    return render(request, 'kumon/inventory.html',context)
