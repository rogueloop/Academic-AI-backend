from django.db import models




class Subject(models.Model):

    DEPARTMENT_CHOICES = (

        ('CSE', 'Computer Science and Engineering'),

        ('MECH', 'Mechanical Engineering'),

        ('IT', 'Information Technology'),
        ('EC', 'Electronics and Communication Engineering'),
        ('EEE', 'Electrical and Electronics Engineering'),
    )

    department = models.CharField(max_length=100, choices=DEPARTMENT_CHOICES)

    subject_code = models.CharField(max_length=10, primary_key=True)

    no_of_modules = models.IntegerField()

    semester = models.IntegerField()

    scheme = models.CharField(max_length=20)

    subject_name = models.CharField(max_length=100)

    credits = models.IntegerField()

    hours = models.IntegerField()
    


class Topic(models.Model):

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    topic_name = models.CharField(max_length=100)

    max_time = models.IntegerField(null=True, blank=True)

    module = models.IntegerField(null=True, blank=True)

    priority = models.IntegerField(null=True, blank=True)

    focus_area = models.BooleanField(blank=True, null=True)

    no_marked_as_important = models.IntegerField(null=True, blank=True)

    no_marked_as_difficult = models.IntegerField(null=True, blank=True)

    no_marked_as_easy = models.IntegerField(null=True, blank=True)
    
    
    


class Batch(models.Model):

    bacth_year=models.CharField(primary_key=True,max_length=50)

    scheme=models.CharField(max_length=20)
    
    

class Exam(models.Model):

    department_name = models.CharField(max_length=100)

    semester = models.CharField(max_length=100,default="")

    series_one_date = models.DateField()

    series_two_date = models.DateField()

    end_semester_date = models.DateField()
    assignment_1_date = models.DateField()

    assignement_2_date = models.DateField()