from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    username = models.CharField(max_length=100, unique=True,)

    class Meta:
        db_table = "Users"
