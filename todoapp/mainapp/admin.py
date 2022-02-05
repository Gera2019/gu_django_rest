from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from mainapp.models import Project, TodoNote, TodoUser


admin.site.register(Project, verbose_name='Проекты')
admin.site.register(TodoNote, verbose_name='Записи')
admin.site.register(TodoUser, UserAdmin)