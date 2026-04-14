from django.db import models

# Create your models here.
class UserModel(models.Model):
    username=models.CharField(max_length=25)
    password=models.CharField(max_length=100)
    profile_picture=models.URLField(max_length=400,null=True)