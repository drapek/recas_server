from notifications.models import NotificationReceiver
from notifications.notifications_clients import SmsAPIClient, MessengerClient


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def send_alert_to_everybody(message, by_sms=False, by_messenger=False):

    everybody = NotificationReceiver.objects.all()

    for receiver in everybody:

        if by_sms and receiver.phone:
            SmsAPIClient.send_message(receiver.phone, message)

        if by_messenger and receiver.messenger_id:
            MessengerClient.send_message(receiver.messenger_id, message)
