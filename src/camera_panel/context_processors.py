from django.conf import settings


def videos_url(request):
    return {'VIDEOS_URL': settings.ABSOLUTE_VIDEOS_URL}
