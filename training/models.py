from ckeditor.fields import RichTextField
from django.db import models
from user.models import User


class CourseModel(models.Model):
    course_title = models.CharField(max_length=255)
    course_description = models.TextField(null=True, blank=True)
    # course_slug = models.SlugField(unique=True)
    date_posted = models.DateTimeField(auto_now_add=True)

