from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.
class Portfolio(models.Model):
    usern=models.ForeignKey(User,on_delete=models.CASCADE,related_name='users')
    firstname=models.CharField(max_length=60)
    lastname=models.CharField(max_length=60)
    resumeurl=models.URLField(max_length=80,unique=True)
    avatar=models.ImageField(upload_to='avatar',default='avatar/defaultavatar.jpg')
    def __str__(self):
        return 'Username : '+self.usern.username+ ' | '+self.firstname+' '+self.lastname
    def save(self):
        super().save()
        img=Image.open(self.avatar.path)
        if img.height>260 and img.width>260:
            output_size=(260,260)
            img.thumbnail(output_size)
            img.save(self.avatar.path)
class BeginnerSkills(models.Model):
    psb=models.ForeignKey(User,on_delete=models.CASCADE,related_name='BeginnerSkills')
    bskill=models.CharField(max_length=15)
    def __str__(self):
        return self.bskill+' | '+self.psb.username
    
class IntermiddateSkills(models.Model):
    psi=models.ForeignKey(User,on_delete=models.CASCADE,related_name='IntermiddateSkills')
    iskill=models.CharField(max_length=15)
    def __str__(self):
        return self.iskill+' | '+self.psi.username

class AdvancedSkills(models.Model):
    psa=models.ForeignKey(User,on_delete=models.CASCADE,related_name='AdvancedSkills')
    askill=models.CharField(max_length=15)
    def __str__(self):
        return self.askill+' | '+self.psa.username

class PortfolioProject(models.Model):
    ps=models.ForeignKey(User,on_delete=models.CASCADE,related_name='portfolioproject')
    pname=models.CharField(max_length=60)
    purl=models.URLField()
    pdesp=models.TextField()
    pimage=models.ImageField(upload_to="projectimage")
    def __str__(self):
        return self.pname + ' | '+self.ps.username

    def save(self):
        super().save()
        img=Image.open(self.pimage.path)
        if img.height>1024 and img.width>768:
            output_size=(1024,768)
            img.thumbnail(output_size)
            img.save(self.pimage.path)
