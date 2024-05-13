from rest_framework import viewsets ,generics
from .models import Subject, Topic,Exam
from .serializers import CourseSerializer, TopicSerializer,ExamSerializer

from rest_framework.response import Response

from rest_framework.decorators import action, APIView, api_view
from student.models import User

from student.models import User,Task
import random
from datetime import timedelta
from rest_framework.decorators import api_view
from .models import Topic, Exam
from .serializers import TopicSerializer
from rest_framework.response import Response


class CourseViewSet(generics.ListCreateAPIView):

    queryset=Subject.objects.all()
    serializer_class = CourseSerializer

    def post(self, request, *args):
        topics_data = request.data.get('topics')
        course_code = request.data.get('course_code')

        # Creating the course instance
        course = Subject.objects.create(
            department=request.data.get('department'),
            subject_code=course_code,
            no_of_modules=request.data.get('no_of_modules'),
            semester=request.data.get('semester'),
            scheme=request.data.get('scheme'),
            subject_name=request.data.get('course_name'),
            hours=request.data.get('hours'),
            credits=request.data.get('credits'),
        )
        students = User.objects.filter(dept=course.department, semester=course.semester)
        


        for topic_data in topics_data:

            topics_list = topic_data.get('topic')

            module = topic_data.get('module')

            priority = request.data.get('credits')

            focus_areas = topic_data.get('focus_area', [])
                

            for topic_name in topics_list:

                random_time = random.randint(20, 40)  # Random time between 2 hours (120 minutes) and 4 hours (240 minutes)

                max_time = random_time

                mintime = 18 # Half of the max_time
                
                #deadline calculation
                    # 1. Get the date of the exams from the exam instance 
                    # 2. Calculate the number of days left for the exam
                
                focus_area = True if topic_name in focus_areas else False

                Topic.objects.create(subject=course, topic_name=topic_name, module=module, focus_area=focus_area,priority=priority)

                if students:

                    for student in students:

                        Task.objects.create(student=student, task_name=topic_name, module=module, deadline=30, max_study_time=max_time, min_study_time=mintime, priority=priority, focus_area=focus_area,subject=course)
                


        serializer = CourseSerializer(course).data

        return Response(serializer)



class TopicViewSet(generics.ListCreateAPIView):

    queryset = Topic.objects.all()

    serializer_class = TopicSerializer
    

class ExamViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer


@api_view(['GET'])
def marked_as_important(request, *args, **kwargs):
    name=request.data.get('topic_name')
    topic = Topic.objects.get(topic_name=name)
    topic.no_marked_as_important += 1
    topic.save()
    return Response({"message":"Marked as important"})


@api_view(['GET'])
def marked_as_difficult(request, *args, **kwargs):
    name=request.data.get('topic_name')
    topic = Topic.objects.get(topic_name=name)
    topic.no_marked_as_difficult += 1
    topic.save()
    return Response({"message":"Marked as difficult"})


@api_view(['GET'])
def marked_as_easy(request, *args, **kwargs):
    name=request.data.get('topic_name')
    topic = Topic.objects.get(topic_name=name)
    topic.no_marked_as_easy += 1
    topic.save()
    return Response({"message":"Marked as easy"})


@api_view(['GET'])
def count_of_importance(request, *args, **kwargs):
    name = request.data.get('topic_name')
    department = request.data.get('department')
    topic = Topic.objects.get(topic_name=name, subject__department=department)
    return Response({"no_of_importance": topic.no_marked_as_important})

@api_view(['GET'])
def next_exam_date(request, **args):
    department = request.data.get('department')
    semester = request.data.get('semester')
    exam = Exam.objects.filter(subject__department=department, subject__semester=semester).order_by('series_one_date') 
    exam_date = exam[0].series_one_date

    # Check if there is any event close to the exam date
    events = ExamSerializer(Exam.objects.filter(exam)).data

    if events:
        return Response({"exam_date": exam_date, "event_close": True})
    else:
        return Response({"exam_date": exam_date, "event_close": False})

