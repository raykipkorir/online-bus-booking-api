# Online booking system API

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
/api/users/ - create and retrieve all users(admin only)
```

```
/api/users/<id>/ - retrieve, update, delete specific user by id (admin only)
```

```
/api/users/me/ - retrieve, update, delete logged in user
```

```
/api/users/set_password/ - change password
```

```
/api/users/reset_password/ - reset password
```
```
password_reset_confirm ???
```

## Booking


## Drivers
```
/api/drivers/ - list and create driver (admin only)
```
```
/api/drivers/<id> - retrieve, update and delete driver (admin only)
```
## Routes
```
/api/routes/ - list and create route (admin only)
```
```
/api/routes/<id> - retrieve, update and delete route (admin only)
```
## Admins
```
/api/admins/ - create new admins (admin only)
```

