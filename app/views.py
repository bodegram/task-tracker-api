from django.shortcuts import render
from .serializer import RegisterSerializer, TaskSerializer, UserSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Task, CustomUser
from rest_framework.permissions import IsAuthenticated
# Create your views here.

@api_view(['POST'])
def register(request):
    if request.method == "POST":
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"message": "Account successfully created"}, status=status.HTTP_201_CREATED)
        
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
@api_view(['GET', 'DELETE', 'POST'])
@permission_classes([IsAuthenticated])
def tasks(request):
    query = Task.objects.filter(user=request.user).all()
    if request.method == "GET":
        serializer = TaskSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == "DELETE":
        query.delete()
        return Response({"message": "Tasks deleted"}, status=status.HTTP_200_OK)
    
    if request.method == "POST":
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"message": "Task created"}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def task(request, id):
    query = Task.objects.get(id=id)
    if request.method == "GET":
        serializer = TaskSerializer(query)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == "PUT":
        serializer = TaskSerializer(query, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"message": "Task updated"}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == "DELETE":
        query.delete()
        return Response({"message": "Task deleted"}, status=status.HTTP_200_OK)
    
    
    
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def profile(request):
    query = CustomUser.objects.get(email=request.user)
    if request.method == "GET":
        serializer = UserSerializer(query)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == "DELETE":
        query.delete()
        return Response({"message": "Account deleted"}, status=status.HTTP_200_OK)
    
    
    if request.method == "PUT":
        serializer = UserSerializer(query, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"message": "Profile updated successfully"}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    
    
    
        
        
        
        
