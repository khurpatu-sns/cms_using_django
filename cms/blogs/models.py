from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class blogs(models.Model):
  title = models.CharField(max_length=25)
  subtitle = models.CharField(max_length=255)
  description = models.TextField()
  image = models.ImageField(upload_to='images', blank=True, null = True)
  author=models.ForeignKey(User,on_delete=models.CASCADE,default=13)
  created_at = models.DateTimeField(auto_now_add=True)
  
  


