# Generated by Django 3.1 on 2008-12-31 20:24

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogpost',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=300)),
                ('thumb', models.ImageField(upload_to='blogthumb')),
                ('content', ckeditor.fields.RichTextField(default='')),
                ('author', models.CharField(max_length=30)),
                ('slug', models.SlugField(default='no-slug', max_length=200, unique=True)),
                ('tag', models.CharField(max_length=500)),
                ('timestamp', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=254)),
                ('website', models.CharField(default='https://127.0.0.1:8000', max_length=60)),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.Blogpost')),
            ],
        ),
    ]
