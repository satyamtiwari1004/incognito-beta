from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .forms import Portfolioform,Beginnerform,Intermiddateform,Advancedform,Portfolioprojectform
from .models import Portfolio,BeginnerSkills,IntermiddateSkills,AdvancedSkills,PortfolioProject
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
# Create your views here.
@login_required(login_url='/accounts/signin/')
def createp(request):
    userid=User.objects.filter(username=request.user).first()
    portfolioname=Portfolio.objects.filter(usern=userid)
    portfolion=Portfolio.objects.filter(usern=userid).first()
    bskills=BeginnerSkills.objects.filter(psb=userid)
    iskills=IntermiddateSkills.objects.filter(psi=userid)
    askills=AdvancedSkills.objects.filter(psa=userid)
    pskills=PortfolioProject.objects.filter(ps=userid)
    lenp=len(portfolioname)
    if lenp==1:
        lengthp=True
    else:
        lengthp=False
    print('lengthp:',lengthp)
    context={'portfolioname':portfolioname,'portfoliona':portfolion,'lengthp':lengthp,'userid':userid,
    'bskills':bskills,'askills':askills,'iskills':iskills,'pskills':pskills}
    return render(request,'user/portfolio_form.html',context)
def seep(request,slug):
    userid=get_object_or_404(User,username=slug)
    portfolioname=Portfolio.objects.filter(usern=userid)
    portfolion=Portfolio.objects.filter(usern=userid).first()
    bskills=BeginnerSkills.objects.filter(psb=userid)
    iskills=IntermiddateSkills.objects.filter(psi=userid)
    askills=AdvancedSkills.objects.filter(psa=userid)
    pskills=PortfolioProject.objects.filter(ps=userid)
    oddno=[1,3,5,7,9,11,13,15]
    evenno=[2,4,6,8,10,12,14,16]
    context={'portfolioname':portfolion,'userid':userid,'bskills':bskills,
             'askills':askills,'iskills':iskills,'pskills':pskills,'oddno':oddno,'evenno':evenno}
    return render(request,'user/index.html',context)
def mycourses(request):
    return render(request,'user/mycourses.html')
def portfoliop(request):
    if request.method =='POST':
        print(request.FILES)
        portfolio_form=Portfolioform(data=request.POST,files=request.FILES)
        print(portfolio_form)
        if portfolio_form.is_valid():
            new_port=portfolio_form.save(commit=False)
            new_port.avatar=request.FILES['avatar']
            new_port.usern=getattr(request, 'user', None)
            new_port.save()
            print(new_port)
    return redirect('/user/createportfolio/')
def Beginnerskills(request):
    try:
        bskil=request.POST['bskill']
        skilllexits=BeginnerSkills.objects.filter(bskill=bskil,psb=request.user).count()
        skilllexits1=IntermiddateSkills.objects.filter(iskill=bskil,psi=request.user).count()
        skilllexits2=AdvancedSkills.objects.filter(askill=bskil,psa=request.user).count()
        if not skilllexits and not skilllexits1 and not skilllexits2:     
            if request.method =='POST':
                b_form=Beginnerform(data=request.POST)
                if b_form.is_valid():
                    new_form=b_form.save(commit=False)
                    new_form.psb=getattr(request, 'user', None)
                    new_form.save()
            return redirect('/user/createportfolio/')
        else:
            return JsonResponse({'skill':'skill'},status=200)
    except Exception as E:
        print(E)
        return JsonResponse({},status=500)
def Intermiddateskills(request):
    try:
        bskil=request.POST['iskill']
        skilllexits=BeginnerSkills.objects.filter(bskill=bskil,psb=request.user).count()
        skilllexits1=IntermiddateSkills.objects.filter(iskill=bskil,psi=request.user).count()
        skilllexits2=AdvancedSkills.objects.filter(askill=bskil,psa=request.user).count()
        if not skilllexits and not skilllexits1 and not skilllexits2:     
            if request.method =='POST':
                b_form=Intermiddateform(data=request.POST)
                if b_form.is_valid():
                    new_form=b_form.save(commit=False)
                    new_form.psi=getattr(request, 'user', None)
                    new_form.save()
            return redirect('/user/createportfolio/')
        else:
            return JsonResponse({'skill':'skill'},status=200)
    except Exception as E:
        print(E)
        return JsonResponse({},status=500)
def Advancedskills(request):
    try:
        bskil=request.POST['askill']
        skilllexits=BeginnerSkills.objects.filter(bskill=bskil,psb=request.user).count()
        skilllexits1=IntermiddateSkills.objects.filter(iskill=bskil,psi=request.user).count()
        skilllexits2=AdvancedSkills.objects.filter(askill=bskil,psa=request.user).count()
        if not skilllexits and not skilllexits1 and not skilllexits2:   
            if request.method =='POST':
                b_form=Advancedform(data=request.POST)
                if b_form.is_valid():
                    new_form=b_form.save(commit=False)
                    new_form.psa=getattr(request, 'user', None)
                    new_form.save()
            return redirect('/user/createportfolio/')
        else:
            return JsonResponse({'skill':'skill'},status=200)
    except Exception as E:
        print(E)
        return JsonResponse({},status=500)
def portfolioproject(request):
    if request.method =='POST':
        pform=Portfolio.objects.filter(usern=request.user).first()
        pr_form=Portfolioprojectform(data=request.POST,files=request.FILES)
        if pr_form.is_valid():
            new_form=pr_form.save(commit=False)
            new_form.pimage=request.FILES['pimage']
            new_form.ps=request.user
            new_form.save()
    return redirect('/user/createportfolio/')
