from django.shortcuts import render, get_object_or_404
from rest_framework.viewsets import ModelViewSet, ViewSet, GenericViewSet
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from .models import Project, TodoNote, TodoUser
from .serializers import ProjectModelSerializer, ProjectModelSerializerIn, TodoNoteModelSerializer, \
    TodoUserModelSerializer, TodoNoteModelSerializerIn, TodoUserModelSerializerStatus
from .filters import ProjectFilter, TodoNoteFilter
from rest_framework import mixins


class TodoUserCustomViewSet(
      mixins.ListModelMixin,
      mixins.RetrieveModelMixin,
      mixins.UpdateModelMixin,
      mixins.CreateModelMixin,
      mixins.DestroyModelMixin,
      GenericViewSet
   ):
    queryset = TodoUser.objects.all()

    def get_serializer_class(self):
        if self.request.version == '0.1':
            return TodoUserModelSerializerStatus
        return TodoUserModelSerializer

class TodoUserModelView(ModelViewSet):
    serializer_class = TodoUserModelSerializer

    def get_queryset(self):
        queryset = TodoUser.objects.all()
        username = self.request.query_params.get('username')
        if username is not None:
            queryset = queryset.filter(username=username)
        return queryset


class ProjectLimitOffsetPagination(LimitOffsetPagination):
   default_limit = 10


class ProjectModelViewSet(ModelViewSet):
   queryset = Project.objects.all()
   serializer_class = ProjectModelSerializerIn
   pagination_class = ProjectLimitOffsetPagination
   filter_class = ProjectFilter

   # def get_serializer_class(self):
   #     if self.request.method in ['GET']:
   #         return ProjectModelSerializer
   #     return ProjectModelSerializerIn


class TodoNoteModelViewSet(ModelViewSet):
   queryset = TodoNote.objects.all()
   serializer_class = TodoNoteModelSerializerIn
   filter_class = TodoNoteFilter

   def get_serializer_class(self):
       if self.request.method in ['GET']:
           return TodoNoteModelSerializer
       return TodoNoteModelSerializerIn

   def destroy(self, request, pk, **kwargs):
      note = get_object_or_404(TodoNote, pk=pk)
      note.is_active = False
      note.save()
      return Response(TodoNoteModelSerializer(note).data)
