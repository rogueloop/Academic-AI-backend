from django.db import models

# Create your models here.
class Student(models.Model):
    student_id = models.CharField(max_length=10)
    student_name = models.CharField(max_length=100)
    dept = models.CharField(max_length=50)
    semester = models.IntegerField()
    scheme = models.CharField(max_length=20)
    credits = models.IntegerField()
    study_time = models.IntegerField()
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    def __str__(self):
        return self.student_name


class Task(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=100)
    max_time = models.IntegerField()
    priority = models.IntegerField()
    prequist= models.CharField(max_length=100)
    focus_area = models.BooleanField()
    def __str__(self):
        return self.task_name