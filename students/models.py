from django.db import models
from students.constants import GENDER_CHOICES, CLASS_CHOICES


class Student(models.Model):
    name = models.TextField()
    age = models.PositiveIntegerField()
    rollno = models.TextField()
    student_class = models.CharField(max_length=10, choices=CLASS_CHOICES)
    gender = models.TextField(choices=GENDER_CHOICES)