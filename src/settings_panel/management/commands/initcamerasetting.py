from django.core.management import BaseCommand

from camera_panel.models import Camera
from core.functions import connect_to_all_cameras
from settings_panel.functions import init_camera_settings


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('camera_name', nargs='?', type=str, default=None)

    def handle(self, *args, **options):
        camera = Camera.objects.get(name=options['camera_name'])
        init_camera_settings(camera)
        self.stdout.write(self.style.SUCCESS('SUCCESS'))
