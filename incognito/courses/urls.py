from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.courseshome,name='courseshome'),
    path('<str:slug>',views.coursedetails,name='coursesdetails')
]
