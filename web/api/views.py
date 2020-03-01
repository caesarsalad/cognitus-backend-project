from rest_framework import viewsets, generics,status
from api.serializers import DataSerializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Data
import requests

class DataViewCreate(generics.CreateAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer

@api_view(['GET'])
def TrainViewGet(request):
    r = requests.get('http://microservice:8080/train')
    return Response(r.json(), status=r.status_code)
    
@api_view(['GET'])
def PredictViewGet(request):
    r = requests.get('http://microservice:8080/predict')
    return Response(r.json(), status=r.status_code)
