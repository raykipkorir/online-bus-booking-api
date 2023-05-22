# Online Bus Booking system API

![Python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![postgresql](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)

Built with Django Rest Framework.

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


## TripBus - Bus scheduled for a certain trip
```
/api/buses/<id>/trip-bus/ (admin only)- All trips for a certain bus
```
```
/api/buses/<id>/trip-bus/<id>/ (admin only) - Retrieve, update or delete a trip for a certain bus
```
```
/api/trip-bus/?from=&to=&travel_date= - Query trips using start, destination and date of travel
```
## Ticket
```
/api/buses/<id>/trip-bus/<id>/tickets/ - Create ticket for a certain trip(all users) or list all tickets for a certain trip(admin only)
```
```
/api/buses/<id>/trip-bus/<id>/tickets/<id> - Retrieve ticket(all users) or update, delete ticket for a certain trip(admin only)
```
# Admin dashboard routes
## Bus
```
/api/buses/ - list and create bus (admin only)
```
```
/api/buses<id> - retrieve, update and delete bus (admin only)
```
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
/api/admins/ - list and create new admins (admin only)
```
```
/api/admins/<id> - retrieve, update and delete admin (admin only)
