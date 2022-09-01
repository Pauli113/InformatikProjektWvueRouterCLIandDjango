from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.
class Course(models.Model):
    module_code = models.CharField(max_length=140)
    module_title = models.CharField(max_length=140)
    module_abbrev = models.CharField(max_length=140)
    module_type = models.CharField(max_length=140)
    credit_points = models.IntegerField()
    language = models.CharField(max_length=140)
    duration_of_module = models.IntegerField()
    recommended_semester = models.IntegerField()
    frequency = models.CharField(max_length=140)
    assessment_methods = models.CharField(max_length=140,default='')


    def __str__(self):
        return self.module_title

    class Meta:
        ordering = ['recommended_semester']


