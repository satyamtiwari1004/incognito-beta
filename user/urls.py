from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('createportfolio/',views.createp),
    path('createportfolio/portfolio/',views.portfoliop),
    path('createportfolio/beginner/',views.Beginnerskills),
    path('createportfolio/intermiddate/',views.Intermiddateskills),
    path('createportfolio/advanced/',views.Advancedskills),
    path('createportfolio/portfoliop/',views.portfolioproject),
    path('viewportfolio/',views.seep),
    path('mycourses/',views.mycourses)
]