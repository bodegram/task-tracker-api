from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password

# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    
   
        
        
    
    
class Task(models.Model):
    title = models.CharField(max_length=1000, null=True)
    description = models.TextField(null=True)
    reminder = models.BooleanField(default=False)
    date = models.DateTimeField(null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    