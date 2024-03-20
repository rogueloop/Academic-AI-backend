from rest_framework import viewsets ,generics
from .models import Course, Topic
from .serializers import CourseSerializer, TopicSerializer
from rest_framework.response import Response
from rest_framework.decorators import action, APIView

class CourseViewSet(generics.ListCreateAPIView):
    queryset=Course.objects.all()
    serializer_class = CourseSerializer

    def post(self, request, *args):
        topics_data = request.data.get('topics')
        course_code = request.data.get('course_code')

        # Creating the course instance
        course = Course.objects.create(
            department=request.data.get('department'),
            course_code=course_code,
            no_of_modules=request.data.get('no_of_modules'),
            semester=request.data.get('semester'),
            scheme=request.data.get('scheme'),
            course_name=request.data.get('course_name'),
            hours=request.data.get('hours'),
            credits=request.data.get('credits'),
        )

        for topic_data in topics_data:
            topics_list = topic_data.get('topic')
            module = topic_data.get('module')
            priority = request.data.get('credits')
            focus_areas = topic_data.get('focus_area', [])
            for topic_name in topics_list:
                focus_area = True if topic_name in focus_areas else False
                Topic.objects.create(course=course, topic_name=topic_name, module=module, focus_area=focus_area,priority=priority)

        serializer = CourseSerializer(course).data
        return Response(serializer)


class TopicViewSet(generics.ListCreateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    
