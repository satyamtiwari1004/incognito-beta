from django.db import models
from PIL import Image

# Create your models here.
class Courses(models.Model):
    name=models.CharField(max_length=60,default='Course Name')
    thumbnail=models.ImageField(upload_to="coursesthumb",default='security_analyst-card-1024x634.jpg')
    weblink=models.URLField(unique=True)
    tag=models.CharField(max_length=60)
    price=models.CharField(max_length=20)
    rating=models.IntegerField()
    owner=models.CharField(max_length=40)

    def __str__(self):
        return self.name +' | '+self.price+' | '+self.owner

    def save(self):
        super().save()
        img=Image.open(self.thumbnail.path)
        if img.height>500 and img.width>360:
            output_size=(500,360)
            img.thumbnail(output_size)
            img.save(self.thumbnail.path)