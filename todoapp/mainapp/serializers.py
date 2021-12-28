from rest_framework import serializers, renderers

from .models import Project, TodoNote, TodoUser

class TodoUserModelSerializer(serializers.ModelSerializer):
    class Meta:
       model = TodoUser
       fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password')


class ProjectModelSerializer(serializers.ModelSerializer):
    users = TodoUserModelSerializer(many=True)

    class Meta:
        model = Project
        fields = ['id', 'name', 'url', 'users']

class ProjectModelSerializerIn(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ['id', 'name', 'url', 'users']


class TodoNoteModelSerializer(serializers.ModelSerializer):
    userid = TodoUserModelSerializer()
    projectid = ProjectModelSerializer()
    class Meta:
        model = TodoNote
        fields = '__all__'