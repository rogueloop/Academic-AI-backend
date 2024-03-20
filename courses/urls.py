
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

urlpatterns = [
    path('courses',views.CourseViewSet.as_view(),name='courses' ),
    path('topic',views.TopicViewSet.as_view(),name='courses')
]
