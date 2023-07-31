from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    number = models.CharField(default=False,max_length=10)
    message = models.TextField()
    def __str__(self):
        return self.name

