from django.views.generic import TemplateView, ListView
from django.views.generic.detail import DetailView

from camera_panel.models import Video


class VideosList(ListView):
    template_name = 'camera_panel/saved_videos_list.html'
    model = Video
    ordering = ["-datetime_started"]
    paginate_by = 50


class OnlineVideoPreview(TemplateView):
    template_name = 'camera_panel/online_video_preview.html'


class SavedVideoPreview(DetailView):
    template_name = 'camera_panel/saved_videos_preview.html'
    queryset = Video.objects.all()
