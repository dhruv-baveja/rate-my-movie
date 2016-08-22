
## API Endpoints

### POST /api/register/

#### Request

```
{
    "username": "testuser",
    "email": "test@email.com",
    "password": "testpass"
}
```

#### Response

_status_: 201
_json_:
```
{
    "username": "testuser",
    "email": "test@email.com"
}
```

### POST /api/movies/

#### Request

```
{
    "title": "movie title",
    "description": "this is description"
}
```

#### Response

_status_: 201
_json_:
```
{
    "title": "movie title",
    "description": "this is description"
}
```

### POST /api/ratings/

#### Request

```
{
    "movie": 1,
    "stars": 4
}
```

#### Response

_status_: 201
_json_:
```
{
    "movie": 1,
    "stars": 4
}
```