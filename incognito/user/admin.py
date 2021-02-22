from django.contrib import admin
from .models import Portfolio,BeginnerSkills,IntermiddateSkills,AdvancedSkills,PortfolioProject
# Register your models here.
admin.site.register(Portfolio)

admin.site.register(BeginnerSkills)
admin.site.register(IntermiddateSkills)
admin.site.register(AdvancedSkills)
admin.site.register(PortfolioProject)
