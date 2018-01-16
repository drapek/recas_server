from django.contrib.auth.models import User
from django.db import models

from camera_panel.models import Camera


class NotificationReceiver(models.Model):
    user = models.ForeignKey(User)
    messenger_id = models.CharField(max_length=512, blank=True)
    phone = models.CharField(max_length=15, blank=True)


class LastNotification(models.Model):
    NON_SPECIFIED = 0
    MOTION_ALERT = 1

    ALERT_TYPES = (
        (NON_SPECIFIED, "non_specified"),
        (MOTION_ALERT, "motion_alert"),
    )

    camera = models.ForeignKey(Camera)
    datetime = models.DateTimeField()
    notification_type = models.IntegerField(choices=ALERT_TYPES, default=NON_SPECIFIED)

