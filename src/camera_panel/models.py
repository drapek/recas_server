from django.conf import settings
from django.db import models
import subprocess


class Camera(models.Model):
    name = models.CharField(max_length=128, unique=True)
    port = models.IntegerField()
    address_ip = models.GenericIPAddressField(null=True)

    def listen_on_stream_socket(self):
        # TODO make in async to handle more than 1 camera
        subprocess.run(["python2", "core/scripts/python2/stream_video_fetcher_worker.py", self.name, str(self.port),
                        "{}/{}.jpg".format(settings.IMAGES_STREAM_FOLDER, self.name), settings.VIDEO_FOLDER])


class Video(models.Model):
    camera = models.ForeignKey(Camera)
    name = models.CharField(max_length=512)
    datetime_started = models.DateTimeField()
