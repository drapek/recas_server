from django.conf.urls import url

from settings_panel import views

urlpatterns = [
    url(r'camera/$', views.CameraSettingsView.as_view(), name='camera_settings'),
    # url(r'server/$', views.ServerSettingsView.as_view(), name='saved_video_preview'),
]
