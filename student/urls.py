from .views import RegisterAPI,LoginAPI,get_topics
from django.urls import path
from knox import views as knox_views

urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('schedule/',get_topics , name='schedule'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall')
]