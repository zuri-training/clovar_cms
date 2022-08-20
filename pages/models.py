from django.db import models
from accounts.models import CustomUser

# Create your models here.
class DefaultTemplates(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=100, blank=True)
    html=models.TextField()
    #css=models.TextField()

class CustomUserTemplates(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=100, blank=True)
    html=models.TextField()
    #css=models.TextField()
    created_by=models.ForeignKey(CustomUser, related_name='CustomUserTemplates', on_delete=models.DO_NOTHING)
