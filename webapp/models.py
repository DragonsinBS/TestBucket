from django.db import models
from enum import Enum

# Create your models here.
class Teacher(models.Model):
    teacher_id=models.IntegerField(primary_key=True)
    teacher_name=models.CharField(max_length=32)

class Course(models.Model):
    course_id=models.IntegerField(primary_key=True)
    course_name=models.CharField(max_length=32)
    teacher_handling_id=models.ForeignKey(Teacher,on_delete=models.CASCADE)

class Student(models.Model):
    student_id=models.IntegerField(primary_key=True)
    student_name=models.CharField(max_length=32)

class Test(models.Model):
    test_id=models.IntegerField(primary_key=True)
    date=models.DateField()
    course_id=models.ForeignKey(Course,on_delete=models.CASCADE,)

class Question(models.Model):
    question_id=models.IntegerField(primary_key=True)
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
    scores=[(1,1),(1,1)]
    score=models.IntegerField(choices=scores,default=1)

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
