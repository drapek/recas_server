import json

from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.signals import post_save
from django.dispatch import receiver

from camera_panel.models import Camera
from settings_panel.tasks import send_command_to_camera


class CameraIntegerSettings(models.Model):
    camera = models.ForeignKey(Camera, on_delete=CASCADE)
    name = models.CharField(max_length=256)
    setting_variable_name = models.CharField(max_length=256)
    value = models.IntegerField()
    min_value = models.IntegerField()
    max_value = models.IntegerField()
    description = models.CharField(max_length=256, blank=True)

    def send_updated_values_to_client_camera(self):
        data = json.dumps({
            self.setting_variable_name: self.value
        })
        send_command_to_camera(self.camera.address_ip, 'settings', data, send_type='post')  # TODO send it in async way


@receiver(post_save, sender=CameraIntegerSettings)
def update_camera_settings(sender, instance, **kwargs):
    instance.send_updated_values_to_client_camera()
