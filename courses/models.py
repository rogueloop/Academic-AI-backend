from django.db import models

# Create your models here.
class Course(models.Model):
    course_id = models.CharField(max_length=10)
    dept = models.CharField(max_length=50)
    no_of_modules = models.IntegerField()
    semester = models.IntegerField()
    scheme = models.CharField(max_length=20)
    course_name = models.CharField(max_length=100)
    credits = models.IntegerField()
    hours = models.IntegerField()
    semester=models.IntegerField()
    
    

class Topic(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    topic_name = models.CharField(max_length=100)
    max_time = models.IntegerField()
    priority = models.IntegerField()
    focus_area = models.BooleanField()
    

    