from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from sqlite3 import IntegrityError
from django.db.utils import IntegrityError as ie
from django.core.mail import EmailMessage
from django.template.loader import render_to_string,get_template
from .tokens import account_activation_token
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
# Create your views here.
def signup(request):
    return render(request,'home/signup.html')
def signin(request):
    return render(request,'home/login.html')
def handlesignup(request):
    try:
        if request.method =='POST':
            username=request.POST['username']
            email=request.POST['email']
            password=request.POST['password']
            passwordconfirm=request.POST['confirmpassword']
            userexists=User.objects.filter(username=username).count()
            if not userexists:
                emailexits=User.objects.filter(email=email).count()
                if not emailexits:
                    print('Email VErified')
                    if password==passwordconfirm and len(password) >=8 and password.isalnum() and password != username:
                        usernam=username.lower()
                        myuser=User.objects.create_user(usernam,email,passwordconfirm)
                        myuser.is_active=False
                        myuser.save()
                        current_site = get_current_site(request)
                        mail_subject = 'Confirm your Incognito account.'
                        messagecon ={              
                        'user': myuser,
                        'domain': current_site.domain,
                        'uid':urlsafe_base64_encode(force_bytes(myuser.pk)),
                        'token':account_activation_token.make_token(myuser),}
                        message=get_template("acc_active_email.html").render(messagecon)
                        to_email = email
                        sender="Team Incognito"
                        sendemail = EmailMessage(mail_subject, message,sender, to=[to_email])
                        sendemail.content_subtype="html"
                        sendemail.send()
                        return JsonResponse({'email':'vemail'},status=200)
                    else:
                    
                        return JsonResponse({'perror':'perror'},status=200)
                else:
                    return JsonResponse({'eemail':'emailexits'},status=200)
            else:
                return JsonResponse({'sqliteerror':'sqerror'},status=200)
        else:
            return JsonResponse({},status=500)
    except IntegrityError:
        return JsonResponse({'integrityerror':'ierror'},status=200)
    except ie:
        return JsonResponse({'sqliteerror':'sqerror'},status=200)
def handlesignin(request):
    try:
        if request.method =='POST':
            loginusername=request.POST['loginusername']
            loginpassword=request.POST['loginpassword']
            usernam=loginusername.lower()
            userexists=User.objects.filter(username=usernam).count()
            if userexists:
                user=authenticate(username=usernam,password=loginpassword)
                if user is not None and 'next1' in request.POST:
                    next1=request.POST['next1']
                    login(request,user,backend=None)
                    urlredirect=next1
                    return JsonResponse({'urlre':urlredirect},status=200)
                else:
                    login(request,user,backend=None)
                    return JsonResponse({'urlre':'/'},status=200)
            else:
                return JsonResponse({'userexists':'userexists'},status=200)
        else:
            context={'loginvalue':'Please enter the correct username and password.'}
            return redirect("/signin",context)
    except (ValueError,AttributeError):
        return JsonResponse({},status=500)
        print('Value Error Occured.')
def handlelogout(request):
    logout(request)
    return redirect('/')

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            return render(request,'home/verifyemail.html')
        else:
            return render(request,'home/invalindlink.html')
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        return render(request,'home/invalindlink.html')
