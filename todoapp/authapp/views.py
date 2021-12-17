from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import TodoUser
from .serializers import TodoUserModelSerializer
from djangorestframework_camel_case.render import CamelCaseJSONRenderer,CamelCaseBrowsableAPIRenderer
from djangorestframework_camel_case.parser import CamelCaseJSONParser,CamelCaseFormParser,CamelCaseMultiPartParser


class TodoUserModelViewSet(ModelViewSet):
   renderer_classes = [CamelCaseJSONRenderer, CamelCaseBrowsableAPIRenderer]
   parser_classes = [CamelCaseJSONParser, CamelCaseFormParser, CamelCaseMultiPartParser]
   queryset = TodoUser.objects.all()
   serializer_class = TodoUserModelSerializer