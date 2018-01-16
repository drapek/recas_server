from settings_panel.models import CameraIntegerSettings


def init_camera_settings(camera):
    CameraIntegerSettings(
        camera=camera,
        name='base video sequence',
        setting_variable_name="STREAM_BASE_UNIT_LENGTH",
        value=0,
        min_value="1",
        max_value="900",  # 15 min
        description="The number of seconds when video is recording after motion detection"
    ).save()

    CameraIntegerSettings(
        camera=camera,
        name='motion detection sensitivity',
        setting_variable_name="TRESHOLD",
        value=0,
        min_value="1",
        max_value="100",  # 15 min
        description="Sensitivity of motion detector. The higher value the more sensitive"
    ).save()

