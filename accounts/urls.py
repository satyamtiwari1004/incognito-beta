from django.contrib import admin
from django.urls import path,include
from . import views
from blog import views as view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/',views.signup),
    path('signin/',views.signin),
    path('createaccount/',views.handlesignup),
    path('verifyuser/',views.handlesignin),
    path('logout/',views.handlelogout),
    path('activate/<uidb64>/<token>/',views.activate, name='activate'),
    path('password-reset/',auth_views.PasswordResetView.as_view(
             template_name='forgotpassword/forgetpassword.html',
             subject_template_name='forgotpassword/passworsub.txt',
             email_template_name='forgotpassword/emailtemplate.html'
             
         ),name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='forgotpassword/mailsent.html'
         ),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='forgotpassword/confirmpassword.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='forgotpassword/successpassword.html'
         ),
         name='password_reset_complete')
             
             
             
    ]
