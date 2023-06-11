from django.db import models


class Client(models.Model):
    # Клиент сервиса: контактный email, фио, комментарий
    name = models.CharField(max_length=100, verbose_name='ФИО')
    email = models.EmailField(verbose_name='Почта')
    comment = models.CharField(max_length=200, verbose_name='Комментарий')

    def __str__(self):
        return f'Клиент {self.name}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ('name',)


class Message(models.Model):
    # Сообщение для рассылки (тема письма, тело письма)

    title = models.CharField(max_length=250)
    body = models.TextField

    def __str__(self):
        return f'Сообщение: {self.title}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ('title',)


class Mailing(models.Model):
    # Рассылка: время рассылки, периодичность, статус рассылки

    class Status(models.TextChoices):  # статус рассылки (завершена, создана, запущена)
        COMPLETED = 'CM', 'Completed'  # устанавливается после завершения
        CREATED = 'CR', 'Created'  # устанавливается после создания
        LAUNCHED = 'LA', 'Launched'  # устанавливается при запуске

    class Frequency(models.TextChoices):  # периодичность (раз в день, раз в неделю, раз в месяц)
        ONCE_A_DAY = 'DA', 'Once a day'
        ONCE_A_WEEK = 'WE', 'Once a week'
        ONCE_A_MONTH = 'MO', 'Once a month'

    time = models.TimeField(verbose_name='Время рассылки', null=False, blank=False)
    frequency = models.CharField(max_length=2,
                                 choices=Frequency.choices,
                                 default=Frequency.ONCE_A_DAY,
                                 verbose_name='Периодичность рассылки'
                                 )
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.CREATED,
                              verbose_name='Статус рассылки'
                              )
    # связи:
    # с Клиентами - многие ко многим (в рассылку могут входить несколько клиентов, клиент может быть в разных рассылках)
    # и Сообщениями - один ко многим (сообщение может входить во много рассылок, в рассылке - одно сообщение)
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='Сообщение', null=False, blank=False)
    clients = models.ManyToManyField(Client, verbose_name='Клиенты', null=False, blank=False)

    # def __str__(self):
    #     return f'Клиент {self.name}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
        ordering = ('-time',)


class MailingAttempt(models.Model):
    # Попытка рассылки (дата и время последней попытки, статус попытки, ответ почтового сервера)

    class Status(models.TextChoices):  # периодичность (раз в день, раз в неделю, раз в месяц)
        ACTIVE = 'AC', 'Active'
        COMPLETED = 'CO', 'Completed'

    time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.ACTIVE,
                              verbose_name='Статус попытки рассылки'
                              )
    server_request = models.CharField(max_length=250)
    # связь с Рассылкой - один ко многим (у рассылки может быть несколько попыток, по расписанию)
    mailing = models.ForeignKey(Mailing, on_delete=models.SET_NULL, null=True)
