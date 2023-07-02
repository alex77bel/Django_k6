from django.urls import reverse_lazy, reverse
from django.views import generic

from mailing.models import Message


class MessageCreateView(generic.CreateView):
    model = Message
    fields = ('title', 'body')
    template_name = 'mailing/form.html'
    success_url = reverse_lazy('mailing:messages')
    extra_context = {
        'title': 'Создание сообщения'
    }


class MessagesView(generic.ListView):
    model = Message
    template_name = 'mailing/messages_list.html'
    extra_context = {
        'title': 'Сообщения'
    }


class MessageDeleteView(generic.DeleteView):
    model = Message
    success_url = reverse_lazy('mailing:messages')
    template_name = 'mailing/confirm_delete.html'
    extra_context = {
        'title': 'Удалить сообщение'
    }


class MessageUpdateView(generic.UpdateView):
    model = Message
    fields = ('title', 'body')
    template_name = 'mailing/form.html'
    extra_context = {
        'title': 'Изменить сообщение'
    }

    def get_success_url(self):
        return reverse('mailing:messages')
