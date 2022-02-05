from django.shortcuts import render, get_object_or_404
from rest_framework.viewsets import ModelViewSet, ViewSet, GenericViewSet
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from .models import Project, TodoNote, TodoUser
from .serializers import ProjectModelSerializer, TodoNoteModelSerializer, TodoUserModelSerializer
from .filters import ProjectFilter, TodoNoteFilter
from rest_framework import mixins
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

class CsrfExemptSesionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return


class TodoUserCustomViewSet(
      mixins.ListModelMixin,
      mixins.RetrieveModelMixin,
      mixins.UpdateModelMixin,
      mixins.CreateModelMixin,
      GenericViewSet
   ):
    queryset = TodoUser.objects.all()
    serializer_class = TodoUserModelSerializer

class TodoUserModelView(ModelViewSet):
    serializer_class = TodoUserModelSerializer

    def get_queryset(self):
        queryset = TodoUser.objects.all()
        username = self.request.query_params.get('username')
        if username is not None:
            queryset = queryset.filter(username=username)
        return queryset

# class TodoUserDetails(ModelViewSet):
#     serializer_class = TodoUserModelSerializer
#
#     def get_queryset(self):
#         username = self.kwargs['username']
#         return TodoUser.objects.filter(username=username)

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
   # authentication_classes = (CsrfExemptSesionAuthentication, BasicAuthentication)

   def destroy(self, request, pk, **kwargs):
      note = get_object_or_404(TodoNote, pk=pk)
      note.is_active = False
      note.save()
      return Response(TodoNoteModelSerializer(note).data)
