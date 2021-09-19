from django.db import models

# Create your models here.

class Comments(models.Model):
    video_Id = models.CharField(max_length=100, blank=True, null=True)
    likes = models.IntegerField(default= 0)
    dislikes = models.IntegerField(default= 0)
    text = models.CharField(max_length=300)