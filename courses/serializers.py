from rest_framework import serializers
from .models import Subject, Topic , Exam

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['module', 'subject', 'topic_name', 'focus_area','priority']
class CourseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Subject
        fields = ('department', 'subject_code', 'no_of_modules', 'semester', 'scheme', 'subject_name', 'hours','credits')

class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'
       

