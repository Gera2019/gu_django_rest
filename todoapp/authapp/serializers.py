from rest_framework.serializers import HyperlinkedModelSerializer
from .models import TodoUser


class TodoUserModelSerializer(HyperlinkedModelSerializer):
   class Meta:
       model = TodoUser
       fields = ('username', 'firstname', 'lastname', 'email')