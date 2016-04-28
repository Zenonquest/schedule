
from django.contrib import admin

from .models import Teacher, Student, Event

admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Event)