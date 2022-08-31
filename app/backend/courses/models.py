from django.db import models

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

    class Meta:
        ordering = ['recommended_semester']


