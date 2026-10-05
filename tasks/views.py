from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer
from .pagination import CustomPagination
from .filters import TaskFilter

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated] # Only authenticated users can access the tasks

    # Custom Pagination
    pagination_class = CustomPagination
    
    # Filtering & Search
    filterset_class = TaskFilter
    search_fields = ['title', 'description']

    # Only access user's own tasks
    def get_queryset(self):
        # To prevent AnonymousUser TypeError
        if getattr(self, 'swagger_fake_view', False):
            return Task.objects.none()
        return Task.objects.filter(user=self.request.user)

    # Assign user automatically when creating task
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
