# ReCaS - server

Reacas is security camera system written in python. This repository contains the server part of the system. 
It is written in Django 1.11. 

## Build project (development)
1. Install these packages using apt-get:
* Python3
* pip3
* postgres database

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
```

4. Install all needed python packages and run the server:
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

5. Run the celery (from catalog with manage.py)
```bash
celery -A config worker -l info
```