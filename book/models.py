from email.policy import default
from django.db import models

# Create your models here.

class Book(models.Model):
    name=models.CharField(max_length=50)
    picture=models.ImageField(default="none")
    author=models.CharField(max_length=20, default="Anonymoys")
    email=models.EmailField(blank=True)
    description=models.TextField(default="My tutorials")


    def __str__(self):
        return self.name 