from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField


class Post(models.Model):
    h1 = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    url = models.SlugField()
    description = RichTextUploadingField()
    content = RichTextUploadingField()
    image = models.ImageField()
    image2 = models.ImageField(default=None)
    image3 = models.ImageField(default=None)
    price = models.CharField(max_length=50, default='Уточняйте у оператора')
    def __str__(self):
        return self.title

class TlgrmUser(models.Model):
    tlgrmUser = models.IntegerField()
    name = models.CharField(max_length=200)