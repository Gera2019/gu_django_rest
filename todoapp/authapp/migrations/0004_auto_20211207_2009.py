# Generated by Django 3.2.9 on 2021-12-07 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0003_auto_20211207_2007'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todouser',
            name='firstname',
        ),
        migrations.AlterField(
            model_name='todouser',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='firstname'),
        ),
    ]
