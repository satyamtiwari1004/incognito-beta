from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Blogpost,Comment
# Register your models here.
admin.site.register(Blogpost)
admin.site.register(Comment)
