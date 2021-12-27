from rest_framework import serializers, renderers

from authapp.models import TodoUser
from authapp.serializers import TodoUserModelSerializer
from .models import Project, TodoNote



class ProjectModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['name', 'url', 'users']


class TodoNoteModelSerializer(serializers.ModelSerializer):
    userid = TodoUserModelSerializer()
    projectid = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = TodoNote
        fields = '__all__'