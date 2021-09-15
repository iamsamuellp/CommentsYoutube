from django.db import models

# Create your models here.

class Comments(models.Model):
    first = models.CharField(max_length=50)
    last = models.CharField(max_length=50)
    text = models.CharField(max_length=300)