from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from mailing.models import Client


class MailingListView(ListView):
    model = Client

