from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Project, TodoNote
from .serializers import ProjectModelSerializer, TodoNoteModelSerializer


class ProjectModelViewSet(ModelViewSet):
   queryset = Project.objects.all()
   serializer_class = ProjectModelSerializer

class TodoNoteModelViewSet(ModelViewSet):
   queryset = TodoNote.objects.all()
   serializer_class = TodoNoteModelSerializer
