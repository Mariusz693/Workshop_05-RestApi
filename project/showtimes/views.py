from django.shortcuts import render
from rest_framework import generics
from .models import Cinema, Screening
from .serializers import CinemaSerializer, ScreeningSerializer

# Create your views here.


class CinemaListView(generics.ListCreateAPIView):
    queryset = Cinema.objects.all()
    # queryset = Cinema.objects.filter()
    serializer_class = CinemaSerializer


class CinemaView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer


class ScreeningListView(generics.ListCreateAPIView):
    queryset = Screening.objects.all()
    serializer_class = ScreeningSerializer


class ScreeningView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Screening.objects.all()
    serializer_class = ScreeningSerializer
