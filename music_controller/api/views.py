from django.shortcuts import render
# from django.http import HttpResponse
from rest_framework import generics
from .models import Room
from .serializers import RoomSerializer

# Create your views here.


# This function is defined/named 'main'
# The function takes in a request
# The function returns a HttpResponse which contains
# The string ("hello")

# def main(request):
#     return HttpResponse("<h1>Hello</h1>")

class RoomView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer