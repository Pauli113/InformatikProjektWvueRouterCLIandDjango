from django.shortcuts import render
from django.http import JsonResponse
from .models import Course

# Create your views here.
def index(request):
    courses = []

    for course in Course.objects.all():
        courses.append({
            'moduleCode': course.module_code,
            'module_title':course.module_title
        })

        return JsonResponse(courses,safe=False)