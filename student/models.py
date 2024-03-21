from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from courses.models import Subject

from .managers import CustomUserManager

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    clg_id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    admission_year = models.IntegerField(null=True, blank=True)
    dept = models.CharField(max_length=50, null=True, blank=True)
    semester = models.IntegerField(null=True, blank=True)
    scheme = models.CharField(max_length=20, null=True, blank=True)
    credits = models.IntegerField(null=True, blank=True)
    study_time = models.IntegerField(null=True, blank=True)
    password = models.CharField(max_length=50, null=True, blank=True)
    is_admin = models.BooleanField(default=False)
    series_1_date = models.DateField(null=True, blank=True)
    series_2_date = models.DateField(null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    USERNAME_FIELD = "clg_id"
    REQUIRED_FIELDS = ['is_admin','is_staff','is_superuser']

    objects = CustomUserManager()

    def __str__(self):
        return self.clg_id


class Task(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    subject=models.ForeignKey(Subject, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=100)
    module = models.IntegerField()
    deadline = models.IntegerField()  
    max_study_time = models.IntegerField()
    min_study_time = models.IntegerField()
    priority = models.IntegerField()
    prequist= models.CharField(max_length=100,blank=True, null=True)
    focus_area = models.BooleanField()
    done= models.BooleanField(default=False)
    def __str__(self):
        return f"{self.task_name} - {self.course.course_name}"
    
