import datetime
import time

from django.core.management import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        while True:
            time.sleep(1)
            print(datetime.datetime.now())

