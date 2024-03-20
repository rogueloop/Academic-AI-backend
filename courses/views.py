
from rest_framework import viewsets
from .models import Course, Topic
from .serializers import CourseSerializer, TopicSerializer
from rest_framework.response import Response
from rest_framework.decorators import action

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @action(detail=True, methods=['post'])
    def add_topics(self, request, pk=None):
        course = self.get_object()
        topics_data = request.data.get('topics')
        for topic_data in topics_data:
            topics_list = topic_data['topic']
            module = topic_data['module']
             
            focus_areas = topic_data.get('focus_area', [])
            for topic_name in topics_list:
                focus_area = True if topic_name in focus_areas else False
                Topic.objects.create(course=course, topic=topic_name, module=module, focus_area=focus_area,)
        serializer = self.get_serializer(course)
        return Response(serializer.data)


class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
 