from django.urls import path
from . import views

urlpatterns=[
        path("",views.index),
        path("teacher/<int:course_id>/create_test",views.create_test),
        path("student/answer_test",views.answer_test),
        path("teacher/dashboard",views.teacher_dashboard),
        path("student/dashboard",views.student_dashboard),
        path("login",views.login_view),
        path("logout",views.logout_view),
        path("teacher/course/<int:course_id>",views.teacher_course),
        path("student/course/<int:course_id>",views.student_course),
        path("student/answer_test/<int:test_id>",views.answer_test),
        path("student/submit_test/<int:test_id>",views.submit_test),
        path("student/responses/<int:test_id>",views.responses_view),
        path("teacher/test_summary/<int:test_id>",views.test_summary),
        path("teacher/view_test/<int:test_id>",views.view_test),
        path("works",views.works)]
