from django.urls import path
from keeper.api.views import TaskAPIView, ProjectAPIView, UserAPIView, DashboardAPIView, MyTaskAPIView


app_name = 'keeper'


urlpatterns = [
    path('tasks', TaskAPIView.as_view(), name='tasks'),
    path('tasks/me', MyTaskAPIView.as_view(), name='tasks_me'),
    path('projects', ProjectAPIView.as_view(), name='projects'),
    path('users', UserAPIView.as_view(), name='users'),
    path('dashboard', DashboardAPIView.as_view(), name='dashboard'),
]
