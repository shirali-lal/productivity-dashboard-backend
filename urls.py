from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

router = DefaultRouter()
router.register('tasks', TaskViewSet, basename='tasks')

urlpatterns = [
    path('', include(router.urls)),
]
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, DashboardSummaryView

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='tasks')

urlpatterns = [
    path('', include(router.urls)),
    path('dashboard/summary/', DashboardSummaryView.as_view(), name='dashboard-summary'),
]
