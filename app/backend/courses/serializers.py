from rest_framework.serializers import ModelSerializer

from .models import Course

class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        #for id field
        #fields = '__all__'
        # to exclude id field
        exclude = ['id']
