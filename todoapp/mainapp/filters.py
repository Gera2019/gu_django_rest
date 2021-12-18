from django_filters import rest_framework as filters
from mainapp.models import Project, TodoNote


class ProjectFilter(filters.FilterSet):
   name = filters.CharFilter(lookup_expr='contains')

   class Meta:
       model = Project
       fields = ['name',]

class TodoNoteFilter(filters.FilterSet):
   name = filters.CharFilter(lookup_expr='contains')

   class Meta:
       model = TodoNote
       fields = ['text']