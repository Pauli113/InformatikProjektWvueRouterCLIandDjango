

from rest_framework.viewsets import ModelViewSet

from .models import Course
from .serializers import CourseSerializer

class CoursesViewSet(ModelViewSet):
    queryset = Course.objects.all().order_by('recommended_semester','module_abbrev')
    serializer_class = CourseSerializer
