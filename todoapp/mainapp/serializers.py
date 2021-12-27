from rest_framework import serializers
from authapp.serializers import TodoUserModelSerializer
from .models import Project, TodoNote


class ProjectModelSerializer(serializers.ModelSerializer):
    users = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='firstname'
    )
    class Meta:
        model = Project
        fields = '__all__'

class TodoNoteModelSerializer(serializers.ModelSerializer):
    userid = TodoUserModelSerializer()
    projectid = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = TodoNote
        fields = '__all__'