from django.core.management import BaseCommand

from core.functions import connect_to_all_cameras


class Command(BaseCommand):
    def handle(self, *args, **options):
        connect_to_all_cameras()
        self.stdout.write(self.style.SUCCESS('SUCCESS'))
