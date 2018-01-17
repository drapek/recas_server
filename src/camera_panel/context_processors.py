from django.conf import settings


def videos_url(request):
    return {'VIDEOS_URL': settings.ABSOLUTE_VIDEOS_URL}


def site_url(request):
    return {'SITE_URL': settings.SITE_URL}
