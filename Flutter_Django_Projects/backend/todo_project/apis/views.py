from django.shortcuts import render
from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer

class TodoGetCreate(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer  # Define serializer_class, not serializer


class TodoUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
