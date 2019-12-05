from django.db import models
from datetime import datetime
from enum import Enum
from django.utils import timezone

# Create your models here.
class Teacher(models.Model):
    teacher_id=models.AutoField(primary_key=True)
    teacher_name=models.CharField(max_length=32)
    def __str__(self):
        return self.teacher_name+'('+str(self.teacher_id)+')'

class Course(models.Model):
    course_id=models.AutoField(primary_key=True)
    course_name=models.CharField(max_length=32)
    teacher_handling_id=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    description=models.CharField(max_length=128)
    def __str__(self):
        return self.course_name

class Student(models.Model):
    student_id=models.AutoField(primary_key=True)
    student_name=models.CharField(max_length=32,default='')
    def __str__(self):
        return self.student_name+'('+str(self.student_id)+')'

class Test(models.Model):
    test_id=models.AutoField(primary_key=True)
    date=models.DateField(default=datetime.now)
    course_id=models.ForeignKey(Course,on_delete=models.CASCADE,)
    active=models.BooleanField(default=True)
    def __str__(self):
        return self.course_id.course_name+'-'+str(self.test_id)

class Question(models.Model):
    question_id=models.AutoField(primary_key=True)
    course_id=models.ForeignKey(Course,on_delete=models.CASCADE)
    question=models.TextField()
    optionA=models.CharField(max_length=32)
    optionB=models.CharField(max_length=32)
    optionC=models.CharField(max_length=32)
    optionD=models.CharField(max_length=32)

    #the below is to be used as enum
    options=[
    ('A','Option A'),
    ('B','Option B'),
    ('C','Option C'),
    ('D','Option D')
    ]
    test_id=models.ForeignKey(Test,on_delete=models.CASCADE)
    answer=models.CharField(max_length=1,choices=options)

class Response(models.Model):
    student_id=models.ForeignKey(Student, on_delete=models.CASCADE)
    test_id=models.ForeignKey(Test, on_delete=models.CASCADE)
    question_id=models.ForeignKey(Question, on_delete=models.CASCADE)
    #the below code is to make multiple foreign keys
    class Meta:
        unique_together=(('student_id','test_id','question_id'))
    #the below is to be used as enum
    options=[
    ('A','Option A'),
    ('B','Option B'),
    ('C','Option C'),
    ('D','Option D')
    ]
    response=models.CharField(max_length=1,choices=options)
    scores=[(0,0),(1,1)]
    score=models.IntegerField(choices=scores)

class TotalScore(models.Model):
    student_id=models.ForeignKey(Student, on_delete=models.CASCADE)
    test_id=models.ForeignKey(Test, on_delete=models.CASCADE)
    #the below code is to make multiple foreign keys
    class Meta:
        unique_together=(('student_id','test_id'))

    total_marks=models.IntegerField(default=0)

class OptedCourse(models.Model):
    student_id=models.ForeignKey(Student,on_delete=models.CASCADE)
    course_id=models.ForeignKey(Course,on_delete=models.CASCADE)
    class Meta:
        unique_together=(('student_id','course_id'))
