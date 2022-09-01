from rest_framework.serializers import ModelSerializer

from .models import Course

class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ['module_code','module_title','module_abbrev','module_type','credit_points',
                   'language','duration_of_module','recommended_semester','frequency',
                   'assessment_method','workload']
                   #todo add coordinators,lecturers,lecture,seminar,practical,excersice,'coordinators','location'