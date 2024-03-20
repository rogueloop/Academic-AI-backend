from rest_framework import serializers
from .models import Course, Topic

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'
class CourseSerializer(serializers.ModelSerializer):
    topics = TopicSerializer(many=True)

    class Meta:
        model = Course
        fields = ('department', 'course_code', 'no_of_modules', 'semester', 'scheme', 'course_name', 'hours', 'topics')

    def create(self, validated_data):
        topics_data = validated_data.pop('topics')
        course = Course.objects.create(**validated_data)
        for topic_data in topics_data:
            topics_list = topic_data['topic']
            module = topic_data['module']
            focus_areas = topic_data.get('focus_area', [])
            for topic_name in topics_list:
                focus_area = True if topic_name in focus_areas else False
                Topic.objects.create(course=course, topic=topic_name, module=module, focus_area=focus_area)
        return course

