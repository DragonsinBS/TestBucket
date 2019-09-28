from django.contrib import admin
from .models import Course, Teacher, Student, Test, Question, Response, TotalScore,OptedCourse
# Register your models here.

admin.site.register(Course)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Test)
admin.site.register(Question)
admin.site.register(Response)
admin.site.register(TotalScore)
admin.site.register(OptedCourse)
