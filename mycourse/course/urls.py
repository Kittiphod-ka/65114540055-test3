from django.urls import path
from .views import *
urlpatterns = [
    path('courses/', course_list, name="course_list"),
]