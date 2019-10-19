from django.urls import path
from . import views

urlpatterns=[
        path("",views.index),
        path("teacher/<int:course_id>/create_test",views.create_test),
        path("student/answer_test",views.answer_test),
        path("teacher/dashboard",views.teacher_dashboard),
        #path("student/dashboard",views.student_dashboard),
        path("login",views.login_view),
        path("logout",views.logout_view),
        path("teacher/course/<int:course_id>",views.teacher_course),]
