__author__ = 'Hernan Y.Ke'
from django.core.management import BaseCommand
from data_collector.models import DataPoint

class Command(BaseCommand):
    def handle(self, *args, **options):
        print('All points')
        print(DataPoint.objects.all())