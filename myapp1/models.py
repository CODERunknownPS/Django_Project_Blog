from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class my_blog(models.Model):

    img = models.ImageField(upload_to= 'pics',null = True)
    title = models.CharField( max_length=100)
    sub_title= models.CharField( max_length=100,null = True)
    dsc = models.TextField()
    date = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.title
    