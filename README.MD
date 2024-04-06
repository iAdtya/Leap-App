```start the workers
celery --app api.tasks worker --loglevel=info -P solo
```

```start the django server
python manage.py runserver
```
