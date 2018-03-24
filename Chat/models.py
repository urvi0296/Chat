from django.db import models
from django.utils import timezone

class Message(models.Model):
    sender = models.CharField(max_length=50,null=False)
    text = models.TextField()
    reciever =  models.CharField(max_length=50,null=False)
    datetime = models.DateTimeField()