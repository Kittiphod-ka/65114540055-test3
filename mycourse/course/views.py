from django.shortcuts import render
from .models import *

# Create your views here.
def course_list(request):
    courses = course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})
