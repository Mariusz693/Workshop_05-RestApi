from django.contrib import admin
from django.urls import path

from .views import MovieListView, MovieView


urlpatterns = [
    path('movies/', MovieListView.as_view()),
    path('movies/<int:pk>/', MovieView.as_view()),
]
