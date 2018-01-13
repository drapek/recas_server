from django.conf.urls import url

from camera_panel import views

urlpatterns = [
    url(r'saved-videos/$', views.VideosList.as_view(), name='saved_videos_list'),
    url(r'saved-video-preview/$', views.OnlineVideoPreview.as_view(), name='saved_video_preview'),
    url(r'online-video-preview/$', views.SavedVideoPreview.as_view(), name='online_video_preview'),
]
