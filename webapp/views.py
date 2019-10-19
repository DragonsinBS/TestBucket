from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.template.loader import get_template
from webapp.models import Course, Test, Question, Teacher
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User, Group
import json

# Create your views here.

def index(request):
    user=request.user
    context=dict()
    context["type"]="student"
    if request.user.is_authenticated:
        if(User.objects.filter(username=user, groups__name='teachers').exists()):
            context["type"]="teacher"
        return redirect(teacher_dashboard)
    return render(request,'webapp/login.html')

def create_test(request,course_id):
    if request.user.is_authenticated:
        return render(request,'webapp/create_test.html')
    return redirect(index)

def login_view(request):
    if request.user.is_authenticated:
        return redirect(index)
    username=request.POST.get('username')
    password=request.POST.get('password')
    user = authenticate(request,username=username, password=password)
    if user is not None:
        login(request,user)
        request.session['user_name']=username
        request.session['member_id'] = user.id
        return redirect(index)
    else:
        return HttpResponse("Your username and password didn't match.")


def answer_test(request):
    questions=[]
    questions.append(Question.objects.filter(course_id=test_id))
    context={
    "questions":questions[0]
    }
    return render(request,'webapp/answer_test.html',context)

def teacher_dashboard(request):
    teacher=Teacher.objects.filter(teacher_name=request.session['user_name'])[0]
    courses=[]
    print(request.session['user_name'])
    courses=Course.objects.filter(teacher_handling_id=teacher)

    context={
    "courses":courses
    }
    return render(request,'webapp/dashboard.html',context)

def teacher_course(request,course_id):
    course=Course.objects.filter(course_id=course_id)[0]
    active_tests=Test.objects.filter(course_id=course_id,active=True)
    completed_tests=Test.objects.filter(course_id=course_id,active=False)
    context={
    "course_title":course.course_name,
    "course_id":course.course_id,
    "active":active_tests,
    "completed":completed_tests
    }
    return render(request,'webapp/course_tests.html',context)

def logout_view(request):
    logout(request)
    return redirect(index)
