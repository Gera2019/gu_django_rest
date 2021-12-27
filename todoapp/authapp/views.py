from django.shortcuts import render, get_object_or_404
from rest_framework.viewsets import ModelViewSet,ViewSet,GenericViewSet
from .models import TodoUser
from .serializers import TodoUserModelSerializer
from djangorestframework_camel_case.render import CamelCaseJSONRenderer,CamelCaseBrowsableAPIRenderer
from djangorestframework_camel_case.parser import CamelCaseJSONParser,CamelCaseFormParser,CamelCaseMultiPartParser
from rest_framework.response import Response
from rest_framework import mixins


# class TodoUserModelViewSet(ModelViewSet):
class TodoUserCustomViewSet(
      mixins.ListModelMixin,
      mixins.RetrieveModelMixin,
      mixins.UpdateModelMixin,
      GenericViewSet
   ):
   queryset = TodoUser.objects.all()
   serializer_class = TodoUserModelSerializer

