from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from PIL import Image

# Create your models here.
class Blogpost(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=300)
    thumb=models.ImageField(upload_to="blogthumb")
    content=RichTextUploadingField(default='')
    author=models.CharField(max_length=30)
    slug=models.SlugField(default='no-slug',unique=True,max_length=200)
    tag=models.CharField(max_length=500)
    timestamp=models.DateTimeField(auto_now_add=True)
    def save(self):
        self.slug=slugify(self.title)
        super(Blogpost,self).save()
        img=Image.open(self.thumb.path)
        if img.height>1024 and img.width>768:
            output_size=(1024,768)
            img.thumbnail(output_size)
            img.save(self.thumb.path)

    def __str__(self):
        return self.title+ ' | '+self.author
class Comment(models.Model):
    post=models.ForeignKey(Blogpost,on_delete=models.CASCADE,related_name='comments')
    name=models.CharField(max_length=60)
    email=models.EmailField()
    website=models.URLField(max_length=60,default='https://127.0.0.1:8000')
    Message=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return 'Comment {} by {} -- '.format(self.Message,self.name)