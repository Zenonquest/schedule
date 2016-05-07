from rest_framework import serializers
from .models import Teacher, Student, Event

class TeacherSerializer(serializers.ModelSerializer):

	class Meta:
		model = Teacher
		fields = ('teacher_id', 'nickname', 
			'monday_start', 'monday_end', 'monday_duration', 
			'tuesday_start', 'tuesday_end', 'tuesday_duration',
			'wednesday_start', 'wednesday_end', 'wednesday_duration',
			'skill_1', 'skill_2', 'skill_3', 'skill_4')

class StudentSerializer(serializers.ModelSerializer):

	class Meta:
		model = Student
		fields = ('student_id', 'student_name', 
			'monday_start', 'monday_end', 'monday_duration', 
			'tuesday_start', 'tuesday_end', 'tuesday_duration',
			'wednesday_start', 'wednesday_end', 'wednesday_duration',
			'skill_1', 'skill_2', 'skill_3', 'skill_4')

class EventSerializer(serializers.ModelSerializer):

	class Meta: 
		model = Event
		fields = ('event_id', 'teacher', 'student', 'start_datetime', 'duration', 'notes')