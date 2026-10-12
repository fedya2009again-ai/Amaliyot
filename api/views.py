from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .models import Category, Comment, Job
from .seralizers import CategorynameSerializer, CategorydetailSerializer, CommentSerializer, JobSerializer, RegisterSerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()

    def get_serializer_class(self):
        if self.kwargs.get("pk"):
            return CategorydetailSerializer
        return CategorynameSerializer



class JobViewSet(ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def get_queryset(self):
        if self.kwargs.get("category_id"):
            return Job.objects.filter(category_id=self.kwargs.get("category_id"))
        return Job.objects.all()



class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer



@api_view(["POST"])
def register(request):
    serializer = RegisterSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






















