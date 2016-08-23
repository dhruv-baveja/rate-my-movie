
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

### POST /api-auth-token/

#### Request

```
{
    "username": "testuser",
    "password": "testpass"
}
```

#### Response

_status_: 200
_json_:
```
{
    "token": "2er89tertweeqt5qtzgdsd98adsfdsgw4t2uqajdj754d",
}
```

### POST /api/movies/

#### Request

_Authorisation_: Token 2er89tertweeqt5qtzgdsd98adsfdsgw4t2uqajdj754d
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

_Authorisation_: Token 2er89tertweeqt5qtzgdsd98adsfdsgw4t2uqajdj754d
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