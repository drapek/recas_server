from django.conf import settings
from django.db import models
import subprocess

from settings_panel.tasks import send_command_to_camera


class Camera(models.Model):
    name = models.CharField(max_length=128, unique=True)
    port = models.IntegerField()
    address_ip = models.GenericIPAddressField(null=True)

    def listen_on_stream_socket(self):
        # TODO make in async to handle more than 1 camera
        subprocess.run(["python2", "core/scripts/python2/stream_video_fetcher_worker.py", self.name, str(self.port),
                        "{}/{}.jpg".format(settings.IMAGES_STREAM_FOLDER, self.name), settings.VIDEO_FOLDER])

    def update_object_using_client_camera_data(self):
        # this shouldn't be assync
        response = send_command_to_camera(self.address_ip, 'settings', send_type='get')
        data = response.json()
        for setting in data:
            setting_object = self.cameraintegersettings_set.filter(setting_variable_name=setting).first()
            if setting_object:
                setting_object.value = data[setting]
                setting_object.save()


class Video(models.Model):
    camera = models.ForeignKey(Camera)
    name = models.CharField(max_length=512)
    datetime_started = models.DateTimeField()

