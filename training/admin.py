from django.contrib import admin
from .models import *


class CourseModelAdmin(admin.ModelAdmin):
    list_display = ('course_title', )
    search_fields = ('course_title',)
    readonly_fields = ()

    filter_horizontal = ()
    ordering = ()
    fieldsets = ()
    list_filter = ()


admin.site.register(CourseModel, CourseModelAdmin)
