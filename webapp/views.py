from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.template.loader import get_template
from webapp.models import Course, Test, Question
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User, Group
# Create your views here.

def index(request):
    user=request.user
    context=dict()
    context["type"]="student"
    if request.user.is_authenticated:
        if(User.objects.filter(username=user, groups__name='teachers').exists()):
            context["type"]="teacher"
        print(context)
        return render(request,'webapp/dashboard.html',context)
    return render(request,'webapp/login.html')

def create_test(request):
    if request.user.is_authenticated:
        return render(request,'webapp/create_test.html')
    return redirect(index)

def login_view(request):
    if request.user.is_authenticated:
        return redirect(index)
    username=request.POST['username']
    password=request.POST['password']
    user = authenticate(request,username=username, password=password)
    if user is not None:
        login(request,user)
        request.session['member_id'] = user.id
        return redirect(index)
    else:
        return HttpResponse("Your username and password didn't match.")


def answer_test(request):
    questions=[]
    questions.append(Question.objects.filter(course_id=1))
    context={
    "questions":questions[0]
    }
    return render(request,'webapp/answer_test.html',context)

def dashboard(request):
    return render(request,'webapp/dashboard.html')


def logout_view(request):
    logout(request)
    return redirect(index)
