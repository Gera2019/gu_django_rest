from django.shortcuts import render, get_object_or_404
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from authapp.models import TodoUser
from .models import Project, TodoNote
from .serializers import ProjectModelSerializer, TodoNoteModelSerializer
from .filters import ProjectFilter, TodoNoteFilter


class ProjectLimitOffsetPagination(LimitOffsetPagination):
   default_limit = 10

class ProjectModelViewSet(ModelViewSet):
   queryset = Project.objects.all()
   serializer_class = ProjectModelSerializer
   pagination_class = ProjectLimitOffsetPagination
   filter_class = ProjectFilter


class TodoNoteModelViewSet(ModelViewSet):
   queryset = TodoNote.objects.all()
   serializer_class = TodoNoteModelSerializer
   filter_class = TodoNoteFilter

   def destroy(self, request, pk, **kwargs):
      note = get_object_or_404(TodoNote, pk=pk)
      note.is_active = False
      note.save()
      return Response(TodoNoteModelSerializer(note).data)
