from django.shortcuts import render,HttpResponse,redirect
from blog import models as md
import webbrowser as wb
import requests
from django.contrib.sites.shortcuts import get_current_site
# Create your views here.
def homepage(request):
    Blogposts=md.Blogpost
    threepost=Blogposts.objects.all().order_by('-sno')[0:4]
    context={'threepost':threepost}
    return render(request,'home/homepage.html',context)
def comingsoonpage(request):
    return render(request,'comingsoon.html')
def proxy(request):
    if request.POST:
        weburl=request.POST['proxyweburl']
        x = requests.post(weburl)
        y = x.text
        print(y)
        f = open("Template/proxytemplate.html", "w+")
        f.write(y)
        f.close()
        return render(request,'proxytemplate.html')
    else:
        return render(request,'courses/proxyhome.html')
def help(request):
    return render(request,'bot.html')

