from django.conf.urls import url, include

from notifications import views

urlpatterns = [
    url(r'notification$', views.GetNotification.as_view(), name='api_receive_notification'),
    url(r'renew-camera-stream/$', views.RenewVideoSteamTTL.as_view(), name='api_renew_camera_stream')
]
