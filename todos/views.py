from django.shortcuts import render
from rest_framework import generics,permissions

from .models import Todo
from .serializers import TodoSerializer

# Create your views here.


class ListTodo(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class DetailsTodo(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer