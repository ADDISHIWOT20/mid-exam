from django.shortcuts import render


from rest_framework import generics
from .models import employee
from .serializers import employeSerializer


# Create your views here.
class employeList(generics.ListCreateAPIView):
    serializer_class=employeSerializer
    queryset = employee.objects.all()

class employeDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class= employeSerializer
    queryset =employee.objects.all()

class employeupdate(generics.RetrieveUpdateDestroyAPIView):
    serializer_class= employeSerializer 
    queryset = employee.objects.all()    