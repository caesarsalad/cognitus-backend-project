from rest_framework import serializers
from api.models import Data

class DataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Data
        fields = ['text']