from urllib import response
from django.shortcuts import render

from .models import Songs
from .serializers import SongSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class SongList(APIView):
    def get(self, request):
        song= Songs.objects.all()
        serializer = SongSerializers(song, many=True)
        return Response(serializer.data)

def post(self, request):
    serializer = SongSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    