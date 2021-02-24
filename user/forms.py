from django import forms
from .models import Portfolio,BeginnerSkills,IntermiddateSkills,AdvancedSkills,PortfolioProject
class Portfolioform(forms.ModelForm):
    firstname=forms.CharField()
    lastname=forms.CharField()
    resumeurl=forms.URLField()
    avatar=forms.ImageField()
    class Meta:
        model=Portfolio
        fields=('firstname','lastname','resumeurl','avatar')
class Beginnerform(forms.ModelForm):
    bskill=forms.CharField()
    class Meta:
        model=BeginnerSkills
        fields=('bskill',)
class Intermiddateform(forms.ModelForm):
    iskill=forms.CharField()
    class Meta:
        model=IntermiddateSkills
        fields=('iskill',)
class Advancedform(forms.ModelForm):
    askill=forms.CharField()
    class Meta:
        model=AdvancedSkills
        fields=('askill',)
class Portfolioprojectform(forms.ModelForm):
    pname=forms.CharField()
    purl=forms.URLField()
    pdesp=forms.Textarea()
    pimage=forms.ImageField()
    class Meta:
        model=PortfolioProject
        fields=('pname','purl','pdesp','pimage')