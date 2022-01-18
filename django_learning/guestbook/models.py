from django.db import models

# Create your models here.



class Message(models.Model):
    pseudo = models.CharField(max_length=200)
    body = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')
