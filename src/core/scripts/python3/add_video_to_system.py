import sys


def save_video_info(camera_name, video_name, timestamp):
    import os
    import django
    from datetime import datetime

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.develop")
    django.setup()

    from camera_panel.models import Camera, Video

    camera = Camera.objects.get(name=camera_name)
    new_video = Video(camera=camera, name=video_name, datetime_started=datetime.fromtimestamp(int(timestamp)))
    new_video.save()
    print("Success")


if __name__ == '__main__':
    save_video_info(sys.argv[1], sys.argv[2], sys.argv[3])
