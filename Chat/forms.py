from django import forms

from .models import Message

class SendForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('text','reciever')
