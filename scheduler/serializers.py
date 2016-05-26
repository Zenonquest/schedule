from rest_framework import serializers
from .models import Teacher, Student, Event, Skill, Availability
from django.contrib.auth.models import User, Group

class TeacherSerializer(serializers.ModelSerializer):
	class Meta:
		model = Teacher
		# field = ('teacher_id')
		# fields = ('teacher_id', 'nickname', 
		# 	'monday_start', 'monday_end', 'monday_duration', 
			# 'tuesday_start', 'tuesday_end', 'tuesday_duration')

class StudentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Student
		# fields = ('student_id', 'student_name', 
		# 	'monday_start', 'monday_end', 'monday_duration', 
		# 	'tuesday_start', 'tuesday_end', 'tuesday_duration',
		# 	'wednesday_start', 'wednesday_end', 'wednesday_duration')

class EventSerializer(serializers.ModelSerializer):
	class Meta: 
		model = Event
		fields = ('event_id', 'teacher', 'student', 'start_datetime', 'end_datetime')

# class OpenEventSerializer(serializers.ModelSerializer):
# 	class Meta: 
# 		model = OpenEvent
# 		fields = ('openevent_id', 'teacher', 'student', 'start_datetime', 'end_datetime')

class SkillSerializer(serializers.ModelSerializer):
	class Meta: 
		model = Skill

class AvailabilitySerializer(serializers.ModelSerializer):
	class Meta: 
		model = Availability

##oauth2
# first we define the serializers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group

