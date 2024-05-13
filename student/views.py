from rest_framework import viewsets , generics
from .models import User, Task
from .serializers import StudentSerializer, TaskSerializer
from .scheduler import schedule

from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import RegisterSerializer
from rest_framework.decorators import api_view
from knox.views import LoginView as KnoxLoginView
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.contrib.auth import login

# Register API

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": StudentSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1],
        })


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        response_data = {
            'token': AuthToken.objects.create(user)[1],
            'user': StudentSerializer(user).data,
           
        }
        return Response(response_data)

class TaskViewSet(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    

@api_view(['GET'])
def get_topics(request):
    """
    Determine the current user by their token, and return ttaheir data
    """
    task=Task.objects.all()
    serial=TaskSerializer(task,many=True).data
    schedules=schedule.Scheduler(3, 0.01, 0.9,0.4,35,serial)
    print(serial)
    schedules.train()
    res = schedules.generate_study_schedule()
    return Response(res) 


@api_view(['POST'])
def feedback(request):
    # Using get() method with a default value to avoid KeyError if 'done' is not in the request data
    done = request.data.get('done', [])
    # Using get() method with a default value to avoid KeyError if 'not_done' is not in the request data
    not_done_list = request.data.get('not_done', [])

    if done:
        # Iterate over the tasks marked as done
        for task_name in done:
            # Search for tasks with the given name
            tasks = Task.objects.filter(task_name=task_name)
            for task in tasks:
                # Set the 'done' attribute of the task to True
                task.done = True
                task.save()

    if not_done_list:
        # Iterate over the tasks marked as not done
        for task_name in not_done_list:
            # Search for tasks with the given name
            tasks = Task.objects.filter(task_name=task_name)
            for task in tasks:
                # Set the 'done' attribute of the task to False
                task.procastination_factor = task.procastination_factor+1
                
                task.save()
    parameter_updation();
    return Response({"message": "Feedback processed successfully"})

def no_of_topic_skiped_by_student():
    tasks=Task.objects.all()
    count=0
    for task in tasks:
        if task.procastination_factor>3:
            count+=1
    return Response({"no_of_topic_skiped_by_student":count})

