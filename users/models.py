from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField


class User(PermissionsMixin, AbstractBaseUser):
    username = models.CharField(
        max_length=150,
        unique=True,
        help_text=
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ,
        validators=[ASCIIUsernameValidator],
        error_messages={
            "unique": "A user with that username already exists.",
        },
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = PhoneNumberField(blank=False)

    is_staff = models.BooleanField(
        "staff status",
        default=False,
        help_text="Designates whether the user can log into this admin site.",
    )
    is_active = models.BooleanField(
        "active",
        default=True,
        help_text=
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ,
    )
    date_joined = models.DateTimeField("date joined", default=timezone.now)

    objects = UserManager()

    # EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name", "phone_number"]
