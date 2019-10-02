from django.urls import path
from . import views

urlpatterns=[
        path("",views.index),
        path("create_test",views.create_test),
        path("answer_test",views.answer_test),
        path("dashboard",views.dashboard)]
