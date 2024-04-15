from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):  # Inherit from ModelSerializer
    class Meta:
        model = Todo
        fields = ['id', 'title', 'description', 'isDone', 'date']
