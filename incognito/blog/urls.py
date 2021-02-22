from django.contrib import admin
from django.urls import path,include
from . import views
from home import views as view
urlpatterns = [
    path('',views.bloghome,name='blogHome'),
    path('',view.homepage,name='Home'),
    path('<str:slug>',views.blogpost,name='blogpost'),
    path('<str:slug>/comment/',views.post_detail,name='blogpost')
    
]
