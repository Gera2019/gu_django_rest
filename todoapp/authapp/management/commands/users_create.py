import json, os
from django.core.management.base import BaseCommand
from authapp.models import TodoUser


JSON_PATH = 'authapp/jsons'

def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), mode='r', encoding='utf8') as infile:
        return json.load(infile)

class Command(BaseCommand):
    def handle(selfself, *args, **options):
        test_users = load_from_json('test_users')

        TodoUser.objects.all().delete()
        for user in test_users:
            new_user = TodoUser(**user)
            new_user.save()

        super_user = TodoUser.objects.create_superuser('admin', 'admin@m.ru', '123', age=30)
        if super_user:
            print('Super-user created')