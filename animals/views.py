from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from animals.serializers import AnimalsSerializer
# Create your views here.
class Animals(APIView):
    permission_classes = (AllowAny,)

def post(self, request):
    data = request.data
    serializer = AnimalsSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


