from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    clg_id = models.CharField(max_length=10,primary_key=True)
    name = models.CharField(max_length=100)
    dept = models.CharField(max_length=50)
    semester = models.IntegerField()
    scheme = models.CharField(max_length=20)
    credits = models.IntegerField()
    study_time = models.IntegerField()

    password = models.CharField(max_length=50)
    is_admin = models.BooleanField(default=False)
    
    
    USERNAME_FIELD = "clg_id"
    REQUIRED_FIELDS = ['is_admin']

    objects = CustomUserManager()

    def __str__(self):
        return self.clg_id


class Task(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=100)
    max_time = models.IntegerField()
    priority = models.IntegerField()
    prequist= models.CharField(max_length=100)
    focus_area = models.BooleanField()
    def __str__(self):
        return self.task_name