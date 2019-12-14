from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.http import HttpResponse, Http404
from django.template.loader import get_template
from webapp.models import Course, Test, Question, Teacher, Student, OptedCourse, Response, TotalScore
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
        return redirect(student_dashboard)
    return render(request,'webapp/login.html')

def create_test(request,course_id):
    course=Course.objects.get(course_id=course_id)
    if request.method=='GET':
        if request.user.is_authenticated:
            back={'there':True,'back':'teacher/course/'+str(course.course_id)}
            return render(request,'webapp/create_test.html',{"course_id":course_id,"back":back})
        return redirect(index)
    count=int(request.POST.get('count'))

    test=Test(course_id=course)
    test.save()

    for ct in range(1,count+1):
        optionA=request.POST.get('question-'+str(ct)+'-A')
        optionB=request.POST.get('question-'+str(ct)+'-B')
        optionC=request.POST.get('question-'+str(ct)+'-C')
        optionD=request.POST.get('question-'+str(ct)+'-D')
        correct=request.POST.get('correct-'+str(ct))
        print(correct)
        question=Question(question=request.POST.get('question-'+str(ct)),test_id=test,course_id=course,optionA=optionA,optionB=optionB,optionC=optionC,optionD=optionD,answer=correct)
        question.save()
    return redirect(teacher_course,course_id=course_id)


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


def answer_test(request,test_id):
    questions=[]
    questions.append(Question.objects.filter(test_id=test_id))
    context={
    "questions":questions[0],
    "test_id":test_id,
    "course_id":questions[0][0].course_id.course_id
    }
    return render(request,'webapp/answer_test.html',context)

def submit_test(request,test_id):
    try:
        responses=[]
        count=Question.objects.filter(test_id=test_id).count()
        print(count)
        test=Test.objects.get(test_id=test_id)
        correct_ans=Question.objects.filter(test_id=test_id)
        correct=[]
        total_score=0
        student_id=Student.objects.get(student_name=request.session['user_name'])
        question0=Question.objects.filter(test_id=test)
        init=question0[0].question_id
        for ct in correct_ans:
            correct.append(ct.answer)
        for ct in range(0,count):
            responses.append(request.POST.get(str(ct+1)))
            print(ct)
            if(responses[ct]!=correct[ct]):
                score=0
                question=Question.objects.get(question_id=ct+init)
                entry=Response(test_id=test,question_id=question,score=score,response=responses[ct],student_id=student_id)
                entry.save()
            else:
                score=1
                total_score+=1
                question=Question.objects.get(question_id=ct+init)
                entry=Response(test_id=test,question_id=question,score=score,response=responses[ct],student_id=student_id)
                entry.save()
        commit_total(test,student_id,total_score)
        return redirect(responses_view,test_id=test.test_id)
    except IntegrityError as e:
        print(e)
        return HttpResponse("youve already given the test")


def commit_total(test,student,score):
    print("here")
    total=TotalScore(student_id=student,test_id=test,total_marks=score)
    total.save()

def responses_view(request,test_id):
    test=Test.objects.get(test_id=test_id)
    course_name=test.course_id.course_name
    course_id=test.course_id.course_id
    student=Student.objects.get(student_name=request.session['user_name'])
    responses=Response.objects.filter(student_id=student,test_id=test)
    questions=Question.objects.filter(test_id=test)
    res_list=[]
    for ct in range(responses.count()):
        res_list.append({"question":questions[ct].question,"correct_option":questions[ct].answer,"selected_option":responses[ct].response,"score":responses[ct].score})
    total=TotalScore.objects.get(test_id=test,student_id=student)
    return render(request,"webapp/responses.html",{"questions":res_list,"total_score":total.total_marks,"test_id":test.test_id,"total":responses.count(),"course_id":course_id,"course_name":course_name,"test":test})

def teacher_dashboard(request):
    teacher=Teacher.objects.filter(teacher_name=request.session['user_name'])[0]
    courses=[]
    courses=Course.objects.filter(teacher_handling_id=teacher)
    context={
    "courses":courses,
    "teacher":True,
    "student":False
    }
    return render(request,'webapp/dashboard.html',context)

def test_summary(request,test_id):
    test=Test.objects.get(test_id=test_id)
    course_id=test.course_id.course_id
    results=TotalScore.objects.filter(test_id=test)
    students=[]
    for res in results:
        student=Student.objects.get(student_id=res.student_id.student_id)
        students.append({"id":student.student_id,"name":student.student_name,"marks":res.total_marks})
    return render(request,"webapp/test_summary.html",{"test_id":test.test_id,"students":students,"course_id":course_id})

def student_dashboard(request):
    student=Student.objects.filter(student_name=request.session['user_name'])[0]
    courses=[]
    opted_courses=OptedCourse.objects.filter(student_id=student)
    for course in opted_courses:
        courses.append(Course.objects.filter(course_id=course.course_id.course_id)[0])
    context={
    "courses":courses,
    "teacher":False,
    "student":True
    }
    return render(request,'webapp/dashboard.html',context)

def view_test(request,test_id):
    test=Test.objects.get(test_id=test_id)
    course=test.course_id
    questions=Question.objects.filter(test_id=test)
    return render(request,"webapp/view_test.html",{"test_id":test_id,"questions":questions,"course":course})


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

def student_course(request,course_id):
    student=Student.objects.get(student_name=request.session['user_name'])
    course=Course.objects.get(course_id=course_id)
    tests=Test.objects.filter(course_id=course)
    completed_tests=list(TotalScore.objects.filter(student_id=student,test_id__in=tests))
    com_values=[]
    if(len(completed_tests)!=0):
        print(completed_tests[0].test_id.test_id)
        for item in completed_tests:
            com_values.append(item.test_id.test_id)
    active_tests=Test.objects.filter(course_id=course_id,active=True).exclude(test_id__in=com_values)
    context={
    "course_title":course.course_name,
    "course_id":course.course_id,
    "active":active_tests,
    "completed":completed_tests,
    "student":True
    }
    return render(request,'webapp/course_tests.html',context)

def logout_view(request):
    logout(request)
    return redirect(index)


def works(request):
    print(request.GET)
    return HttpResponse(request.GET)
