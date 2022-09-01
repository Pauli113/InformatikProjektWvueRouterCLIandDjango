

from rest_framework.viewsets import ModelViewSet

from .models import Course
from .serializers import CourseSerializer

class CoursesViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
