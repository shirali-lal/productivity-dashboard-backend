from rest_framework import viewsets, permissions
from .models import Task
from .serializers import TaskSerializer
from datetime import date

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Task.objects.filter(user=self.request.user)

        status = self.request.query_params.get('status')
        priority = self.request.query_params.get('priority')
        search = self.request.query_params.get('search')

        if status:
            queryset = queryset.filter(status=status)

        if priority:
            queryset = queryset.filter(priority=priority)

        if search:
            queryset = queryset.filter(title__icontains=search)

        return queryset

    def perform_create(self, serializer):
        task = serializer.save(user=self.request.user)

        if task.deadline < date.today() and task.status != 'Completed':
            task.is_overdue = True
            task.save()
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils.timezone import now
from .models import Task


class DashboardSummaryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        total_tasks = Task.objects.filter(user=user).count()
        completed_tasks = Task.objects.filter(user=user, status="Completed").count()
        pending_tasks = Task.objects.filter(user=user, status="Pending").count()
        overdue_tasks = Task.objects.filter(user=user, status__in=["Pending", "In Progress"], deadline__lt=now()).count()

        completion_rate = 0
        if total_tasks > 0:
            completion_rate = (completed_tasks / total_tasks) * 100

        return Response({
            "total_tasks": total_tasks,
            "completed_tasks": completed_tasks,
            "pending_tasks": pending_tasks,
            "overdue_tasks": overdue_tasks,
            "completion_rate": round(completion_rate, 2)
        })
