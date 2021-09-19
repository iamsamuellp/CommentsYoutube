from django.db import models

# Create your models here.
class Reply(models.Model):
  reply = models.CharField(max_length=300)
  video_Id = models.CharField(max_length=100)
  comment = models.ForeignKey('comments.Comments', blank=True, null=True, on_delete=models.CASCADE)