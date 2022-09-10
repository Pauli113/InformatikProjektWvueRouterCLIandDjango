from email.policy import default
from django.db import models

from jsonfield import JSONField

# Create your models here.
class Course(models.Model):
    module_code = models.CharField(max_length=140)
    module_title = models.CharField(max_length=140)
    module_abbrev = models.CharField(max_length=140)
    module_type = models.CharField(max_length=140)
    credit_points = models.IntegerField(default=0)
    language = models.CharField(max_length=140)
    duration_of_module = models.IntegerField()
    recommended_semester = models.IntegerField()
    frequency = models.CharField(max_length=140)
    coordinators = models.JSONField(default='')
    lecturers = models.JSONField(default='')
    assessment_method = models.CharField(max_length=140,default='')
    workload = models.IntegerField()
    seminar = models.IntegerField(default=0)
    practical = models.IntegerField(default=0)
    excercise = models.IntegerField(default=0)
    self_study = models.IntegerField(default=0)
    required_prerequisites = models.JSONField(default='')
    recommended_prerequisites = models.JSONField(null=True,default='')
    status = models.CharField(max_length=140,default='')
    location = models.CharField(max_length=140,default='')
    po = models.CharField(max_length=140,default='')
    furtherInformation = models.CharField(max_length=1000,default='')
