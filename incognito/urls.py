from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from home import views as view
from user import views as view1

admin.site.site_header = "Incognito Admin"
admin.site.site_title = "Incognito Admin Page"
admin.site.index_title = "Welcome to Incognito"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/',include('blog.urls')),
    path('',include('home.urls')),
    path('accounts/',include('accounts.urls')),
    path('courses/',include('courses.urls')),
    path('comingsoon/',view.comingsoonpage),
    path('proxy/',view.proxy),
    path('help/',view.help),
    path('ckdeditor/',include('ckeditor_uploader.urls')),
    path('user/',include('user.urls')),
    path('<str:slug>/',view1.seep)
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
