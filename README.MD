## Output processed by the celery worker picked from rabbitmq which is message queue

![Screenshot of my app](Screenshot%202024-04-08%20041717.png)

## start the workers

```
celery --app api.tasks worker --loglevel=info -P solo
```

## this didn't

```
celery -A tasks worker --loglevel=INFO
```

## start the django server

```
python manage.py runserver
```
