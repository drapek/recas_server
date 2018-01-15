from camera_panel.models import Camera


def connect_to_all_cameras():
    """
    This should be runed on django startup
    :return:
    """
    [camera.listen_on_stream_socket() for camera in Camera.objects.all()]
