from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated] # Only authenticated users can access the tasks

    # Only access user's own tasks
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    # Assign user automatically when creating task
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
