from .views import RegisterAPI, LoginAPI, TaskViewSet, get_topics, analytics, Total_users, Average_task_done, completed_task
from django.urls import path
from knox import views as knox_views

urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('schedule/',get_topics , name='schedule'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('task/', TaskViewSet.as_view() , name='task'),
    path('analytics/',analytics , name='analytics'),
    path('total_users/',Total_users , name='total_users'),
    path('average_task_done/',Average_task_done , name='average_task_done'),
    path('completed_task/',completed_task , name='completed_task'),
]