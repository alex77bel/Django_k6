from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import client_views
from mailing.views import message_views
from mailing.views import mailing_views

app_name = MailingConfig.name

urlpatterns = [
    path('clients/', client_views.ClientsView.as_view(), name='clients'),
    path('clients/create/', client_views.ClientCreateView.as_view(), name='create_client'),
    path('clients/update/<int:pk>', client_views.ClientUpdateView.as_view(), name='update_client'),
    path('clients/delete/<int:pk>', client_views.ClientDeleteView.as_view(), name='delete_client'),

    path('messages/', message_views.MessagesView.as_view(), name='messages'),
    path('messages/create/', message_views.MessageCreateView.as_view(), name='create_message'),
    path('messages/update/<int:pk>', message_views.MessageUpdateView.as_view(), name='update_message'),
    path('messages/delete/<int:pk>', message_views.MessageDeleteView.as_view(), name='delete_message'),

    path('mailings/', mailing_views.MailingsView.as_view(), name='mailings'),
    path('mailings/create/', mailing_views.MailingCreateView.as_view(), name='create_mailing'),
    path('mailings/update/<int:pk>', mailing_views.MailingUpdateView.as_view(), name='update_mailing'),
    path('mailings/delete/<int:pk>', mailing_views.MailingDeleteView.as_view(), name='delete_mailing'),


    path('', client_views.ClientsView.as_view(), name='main'),

]
