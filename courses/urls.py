
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

urlpatterns = [
    path('courses',views.CourseViewSet.as_view(),name='courses' ),
    path('topic',views.TopicViewSet.as_view(),name='courses'),
    # path('exam',views.ExamViewSet.as_view(),name='courses'),
    path('exams', views.ExamViewSet.as_view({'get': 'list', 'post': 'create'}), name='exams'),
    path('mark_as_important',views.marked_as_important,name='mark_as_important'),
    path('mark_as_difficult',views.marked_as_difficult,name='mark_as_difficult'),
    path('mark_as_easy',views.marked_as_easy,name='mark_as_easy'),
    path('important',views.count_of_importance,name='important'),
]
