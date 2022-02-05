from django.db import models
from django.contrib.auth.models import AbstractUser

class TodoUser(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatars', blank=True)
    age = models.PositiveIntegerField(verbose_name='age', default=18)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.first_name

class Project(models.Model):
    name = models.CharField(
        max_length=64,
        verbose_name='название',
        unique=True,
    )
    url = models.URLField(
        max_length=512,
        verbose_name='git url',
    )
    users = models.ManyToManyField(TodoUser, blank=True)

    def __str__(self):
        return self.name


class TodoNote(models.Model):
    projectid = models.ForeignKey(Project, models.PROTECT)
    userid = models.ForeignKey(TodoUser, models.PROTECT)
    text = models.TextField(
        verbose_name='текст заметки',
    )

    created = models.DateTimeField(
        auto_now_add=True
    )

    updated = models.DateTimeField(
        auto_now=True
    )
    is_active = models.BooleanField(verbose_name='активна', default=True)