import datetime

from django.conf import settings
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from camera_panel.models import Camera
from notifications.functions import get_client_ip, send_alert_to_everybody
from notifications.models import LastNotification


class GetNotification(APIView):
    def post(self, request):
        ip = get_client_ip(request)
        camera = Camera.objects.filter(address_ip=ip).first()
        if not camera:
            return Response({'success': False, 'error': 'Camera of this ip is not existing on the server'},
                            status=HTTP_400_BAD_REQUEST)

        notification_type = request.data.get('notification_type')

        if not notification_type:
            return Response({'success': False, 'error': 'notification_type is required'}, status=HTTP_400_BAD_REQUEST)

        if notification_type == 'motion_alert':
            last_motion_alert = LastNotification.objects.filter(camera=camera,
                                                                notification_type=LastNotification.MOTION_ALERT).first()
            if last_motion_alert is None \
                    or timezone.now() > last_motion_alert.datetime + \
                            datetime.timedelta(minutes=settings.MOTION_ALERT_SUSPENSION_TIME):
                send_alert_to_everybody('Oh crap! Motion detected. Please check the camera if everything is fine.',
                                        by_sms=True, by_messenger=True)

            # Create or update the LastMotion Object
            if last_motion_alert is None:
                LastNotification.objects.create(camera=camera, datetime=timezone.now(),
                                                notification_type=LastNotification.MOTION_ALERT)
            else:
                last_motion_alert.datetime = timezone.now()
                last_motion_alert.save()
        return Response({'success': True})
