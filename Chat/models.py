from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class Message(models.Model):
    text = models.TextField()
    datetime = models.DateTimeField()
    sender = models.ForeignKey(User, related_name='messages_sent',on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='messages_received',on_delete=models.CASCADE)