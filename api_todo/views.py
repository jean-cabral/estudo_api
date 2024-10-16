from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status,viewsets

from .models import Todo
from .serializers import TodoSerializer

import json


@api_view(['GET', 'POST'])
def get_todos(request):

    if request.method == 'GET':

        todos = Todo.objects.all()

        serializer = TodoSerializer(todos, many=True)

        return Response(serializer.data)

    if request.method == 'POST':
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)