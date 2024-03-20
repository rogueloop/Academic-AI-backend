from django.db import models



class Course(models.Model):
    DEPARTMENT_CHOICES = (
        ('CSE', 'Computer Science and Engineering'),
        ('MECH', 'Mechanical Engineering'),
        ('IT', 'Information Technology'),
        ('EC', 'Electronics and Communication Engineering'),
        ('EEE', 'Electrical and Electronics Engineering'),
    )
    department = models.CharField(max_length=100, choices=DEPARTMENT_CHOICES)
    course_code = models.CharField(max_length=10, primary_key=True)
    no_of_modules = models.IntegerField()
    semester = models.IntegerField()
    scheme = models.CharField(max_length=20)
    course_name = models.CharField(max_length=100)
    credits = models.IntegerField()
    hours = models.IntegerField()
    

class Topic(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    topic_name = models.CharField(max_length=100)
    max_time = models.IntegerField()
    module = models.IntegerField()
    priority = models.IntegerField()
    focus_area = models.BooleanField()
    
    


    