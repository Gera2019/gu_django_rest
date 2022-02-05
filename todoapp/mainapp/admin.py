from django.contrib import admin
from mainapp.models import Project, TodoNote

admin.site.register(Project, verbose_name='Проекты')
admin.site.register(TodoNote, verbose_name='Записи')