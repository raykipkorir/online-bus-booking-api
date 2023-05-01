# Ticketing system API

![Python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![postgresql](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)

Build with Django Rest Framework.

# Overview

# Endpoints

## Authentication

```
/api/token/  - to login users
```

```
/api/token/refresh/
```

## Users

```
/users/ - create and retrieve all users(admin only)
```

```
/users/<id>/ - retrieve, update, delete specific user by id (admin only)
```

```
/users/me/ - retrieve, update, delete logged in user
```

```
/users/set_password/ - change password
```

```
/users/reset_password/ - reset password
```

password_reset_confirm ???
