from django.shortcuts import render
from rest_framework import generics,permissions

from .models import Todo
from .serializers import TodoSerializer
from .todo_permissions import IsAuthorOrReadOnly

# Create your views here.


class ListTodo(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class DetailsTodo(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,IsAuthorOrReadOnly,)
    #permission_classes = (IsAuthorOrReadOnly,)
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer