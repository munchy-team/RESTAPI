from django.shortcuts import render
from rest_framework import generics
from .models import MucnhyTest
from .serializers import MunchySeriallizer

class MunchyList(generics.ListCreateAPIView):
    queryset = MucnhyTest.objects.all()
    serializer_class = MunchySeriallizer


class MunchyAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = MucnhyTest.objects.all()
    serializer_class = MunchySeriallizer
# Create your views here.
