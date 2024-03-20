from rest_framework import serializers
from .models import Course, Topic

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['module', 'course', 'topic_name', 'focus_area','priority']
class CourseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Course
        fields = ('department', 'course_code', 'no_of_modules', 'semester', 'scheme', 'course_name', 'hours','credits')


        

