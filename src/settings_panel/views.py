from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView, View

from camera_panel.models import Camera
from settings_panel.models import CameraIntegerSettings


class CameraSettingsView(View):
    template_name = 'settings_panel/camera_settings.html'

    def get(self, request, *args, **kwargs):
        camera_name = request.GET.get('camera_name')
        if camera_name:
            camera = get_object_or_404(Camera, name=camera_name)
        else:
            camera = Camera.objects.first()

        # Update the camera settings from remote client
        camera.update_object_using_client_camera_data()
        integer_settings = CameraIntegerSettings.objects.filter(camera=camera).all()
        return render(request, self.template_name, {"integer_settings": integer_settings})

    def post(self, request):
        for integer_setting_id in self.request.POST:
            try:
                setting = CameraIntegerSettings.objects.get(pk=integer_setting_id)
                setting.value = self.request.POST[integer_setting_id]
                setting.save()
            except Exception as e:
                print(e)
        return self.get(request)
