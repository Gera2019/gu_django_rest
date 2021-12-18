from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
from datetime import timedelta

class TodoUser(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatars', blank=True)
    age = models.PositiveIntegerField(verbose_name='age', default=18)
    firstname = AbstractUser.first_name
    lastname = AbstractUser.last_name
    email = models.EmailField(unique=True)
