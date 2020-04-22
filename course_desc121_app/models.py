from __future__ import unicode_literals
from django.db import models

class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 5:
            errors['name'] = "Course name should be at least 5 characters"
        if len(postData['desc']) < 15:
            errors['desc'] = "Course description should be at least 15 characters"
        return errors

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()

# class Description(models.Model):
#     description = models.OneToOneField(Course, on_delete=models.CASCADE, primary_key=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
    

    

# Create your models here.
