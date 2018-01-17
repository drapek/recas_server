# ReCaS - server

Reacas is security camera system written in python. This repository contains the server part of the system. 
It is written in Django 1.11. 

## Build project (in development mode)
1. Install these packages using apt-get:
```bash
sudo apt-get update
sudo apt-get install python2 python3 postgresql redis ffmpeg libopencv-dev python-opencv
```

2. Create database and database user:
```sql
CREATE ROLE db_username WITH LOGIN PASSWORD "<bd_password>"
CREATE DATABASE <db_name> WITH OWNER;
```
3. Create .env file with credentials (in src folder). It should contain:
```text 
DB_NAME = 'db_name'
DB_USERNAME = 'db_username'
DB_PASSWORD = 'db_password'
SECRET_KEY = 'random_long_stirng'
MESSENGER_ACCESS_TOKEN = 'messenger_token_from_the_app'
SMSAPI_PSWD_MD5 = 'smsapi.pl password in MD5'
SMSAPI_USERNAME = 'smsapi.pl username'
```

4. Install all needed python packages and run the server (in development environment):
```bash
pip install -r requirements.txt
export DJANGO_SETTIGNS_MODULE=config.settings.develop
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8000
# This command will starts workers which will be listening for streaming videos from cameras.
python3 manage.py connectcameras 
```

5. Run the celery (from catalog with manage.py)
```bash
celery -A config worker -l info
```

6. Add your camera data using shell
```bash
python3 manage.py shell
```
using this code:
```python
from camera_panel.models import Camera
Camera(name=<camera name>, port=<camera_port>, address_ip=<camera_ip>).save()
```
```bash
python3 manage.py initcamerasetting <camera_name>
```
# Important notices
* Make sure that `PYTHON3_PROJECT_INTERPRETER` variable in `core/scripts/python2/stream_video_fetcher_worker.py` is properly configured
  It should points to python3 which is used to run the django server