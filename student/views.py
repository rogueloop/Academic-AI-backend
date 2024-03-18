from rest_framework import viewsets
from .models import User, Task
from .serializers import StudentSerializer, TaskSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = StudentSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
