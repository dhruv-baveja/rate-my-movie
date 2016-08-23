# Remind me later

An app where people can add movies and other people can rate them.User can add a movie and other people, except the creator, can rate it. And remember a user can only rate a movie once. Sends the average rating of each movie to all of the creators, at midnight daily.

## Run it!

First start your Redis server
```sh
redis-server
```

Next, start a Celery worker
```sh
python manage.py celeryd
```

Next, start a Celery scheduler
```sh
python manage.py celerybeat
```

Start your Django developement server
```sh
python manage.py runserver
```

