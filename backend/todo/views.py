from django.shortcuts import render
from rest_framework import viewsets
from .serializers import Tblemployeeprofile1Serializer
from .models import Tblemployeeprofile1

class TodoView(viewsets.ModelViewSet):
    serializer_class = Tblemployeeprofile1Serializer
    queryset = Tblemployeeprofile1.objects.all()