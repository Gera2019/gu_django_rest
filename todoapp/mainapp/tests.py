from django.test import TestCase
import json
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
from mixer.backend.django import mixer
from .views import TodoUserModelView
from .models import TodoUser, Project, TodoNote


class TestTodoUserViewSet(TestCase):
    ## APIRequestFactory
    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/viewsets/users/')
        view = TodoUserModelView.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_guest(self):
        factory = APIRequestFactory()
        request = factory.post('/viewsets/users/', {'username': 'guga', 'firstName':'Guga', 'email': 'guga@m.ru'}, format='json')
        view = TodoUserModelView.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_admin(self):
        factory = APIRequestFactory()
        request = factory.post('/viewsets/users/', {'username': 'jinja', 'firstName':'Jiga', 'email': 'jinja@m.ru', 'password': 'a3d3d5g5'}, format='json')
        admin = TodoUser.objects.create_superuser(username='admin',password='rest1243')
        force_authenticate(request, admin)
        view = TodoUserModelView.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    ## APIClient
    def test_get_detail(self):
        user = TodoUser.objects.create(username='jinja', email='jinja@m.ru')
        project = Project.objects.create(name='GGG',url='http://mail.ru')
        project.users.set((user,))
        note = TodoNote.objects.create(userid=user,projectid=project,text='RER')
        client = APIClient()
        response = client.get(f'/viewsets/notes/{note.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_guest(self):
        user = TodoUser.objects.create(username='Yub', email='yub@m.ru')
        client = APIClient()
        response = client.put(f'/viewsets/users/{user.id}/', {'username': 'Грин', 'email': 'grin@m.ru'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

## APITestCase

class TestProjectViewSet(APITestCase):

    def test_get_list(self):
        response = self.client.get('/viewsets/projects/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_admin(self):
        user = TodoUser.objects.create(username='Yub', email='yub@m.ru')
        project = Project.objects.create(name='GGG',url='http://mail.ru')
        project.users.set((user,))
        admin = TodoUser.objects.create_superuser('admin', 'admin@admin.com', 'admin123456')
        self.client.login(username='admin', password='admin123456')
        response = self.client.put(f'/viewsets/projects/{project.id}/', {'name':'JKI','url':'http://mail.ru'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        project = Project.objects.get(id=project.id)
        self.assertEqual(project.name, 'JKI')

    def test_edit_mixer(self):
        project = mixer.blend(Project)
        admin = TodoUser.objects.create_superuser('admin', 'admin@admin.com', 'admin123456')
        self.client.login(username='admin', password='admin123456')
        response = self.client.put(f'/viewsets/projects/{project.id}/', {'name': 'JKI','url':'http://mail.ru'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        project = Project.objects.get(id=project.id)
        self.assertEqual(project.name, 'JKI')

    def test_get_detail(self):
        note = mixer.blend(TodoNote, text='Workspace associated with branch \'lesson_8\' has been restored')
        response = self.client.get(f'/viewsets/notes/{note.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_note = json.loads(response.content)
        self.assertEqual(response_note['text'], 'Workspace associated with branch \'lesson_8\' has been restored')

    def test_get_detail_note(self):
        note = mixer.blend(TodoNote, userid__first_name='Грин')
        response = self.client.get(f'/viewsets/notes/{note.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_note = json.loads(response.content)
        self.assertEqual(response_note['userid']['firstName'], 'Грин')

