from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import teacher
from .serializers import teacherSerializer


class teacherList(generics.ListCreateAPIView):
    serializer_class=teacherSerializer
    queryset = teacher.objects.all()

class teacherDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class= teacherSerializer
    queryset =teacher.objects.all()

class teacherupdate(generics.RetrieveUpdateDestroyAPIView):
    serializer_class= teacherSerializer
    queryset = teacher.objects.all()    