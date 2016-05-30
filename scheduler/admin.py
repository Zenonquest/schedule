
from django.contrib import admin

from .models import Teacher, Student, Event, Availability, Skill, CredentialsModel

admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Event)
admin.site.register(CredentialsModel)
admin.site.register(Availability)
admin.site.register(Skill)
