from django.db import models

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    postedat=models.DateField()
    postby=models.CharField(max_length=100)
    likecount=models.IntegerField()
class Likemodel(models.Model):
    likepostid=models.IntegerField()
    likedbyid=models.TextField()
