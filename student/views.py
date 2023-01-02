from rest_framework import generics
from .models import student
from .serializer import StudentSerializer


# Create your views here.
class StudentList(generics.ListCreateAPIView):
    serializer_class=StudentSerializer
    queryset = student.objects.all()

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class= StudentSerializer
    queryset =student.objects.all()

class Studentupdate(generics.RetrieveUpdateDestroyAPIView):
    serializer_class= StudentSerializer 
    queryset = student.objects.all()    