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
    max_time = models.IntegerField(null=True, blank=True)
    module = models.IntegerField(null=True, blank=True)
    priority = models.IntegerField(null=True, blank=True)
    focus_area = models.BooleanField(blank=True, null=True)
    
    

class Batch(models.Model):
    bacth_year=models.CharField(primary_key=True,max_length=50)
    scheme=models.CharField(max_length=20)
    
    
class Exams(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    duration = models.IntegerField()
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    semester = models.IntegerField()
    subject = models.ForeignKey(Course, on_delete=models.CASCADE)
    exam_type = models.CharField(max_length=100)
    exam_credits = models.IntegerField(blank=True)
    
    def __str__(self):
        return self.name