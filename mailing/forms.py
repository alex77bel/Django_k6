from django import forms
from mailing import models


class ClientForm(forms.ModelForm):
    class Meta:
        model = models.Client
        fields = ('name', 'email', 'comment')


class MessageForm(forms.ModelForm):
    class Meta:
        model = models.Message
        fields = ('title', 'body')

class MailingForm(forms.ModelForm):
    class Meta:
        model = models.Mailing
        fields = ('time', 'frequency', 'clients', 'message')

