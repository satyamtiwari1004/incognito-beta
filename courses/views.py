from django.shortcuts import render,HttpResponse
from .models import Courses
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='/accounts/signin/')
def courseshome(request):
    course=Courses.objects.all().order_by('-id')
    coursefree=Courses.objects.filter(tag='Free').order_by('-id')
    coursePremium=Courses.objects.filter(tag='Premium').order_by('-id')
    five=5
    four=4
    three=3
    context={'course':course,'cf':coursefree,'cp':coursePremium,'fi':five,'fo':four,'thr':three}
    return render(request,'courses/courseshome.html',context)
def coursedetails(request,slug):
    return HttpResponse(f'Its working :'+slug)