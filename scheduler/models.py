from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Teacher(models.Model):
	teacher_id = models.AutoField(primary_key=True)
	nickname = models.CharField(max_length=200, unique=True)
	#Teacher's schedule: available start, availabe end, max duration(default=end-start)
	monday_start = models.TimeField('monday start', null=True, blank=True)
	monday_end = models.TimeField('monday end', null=True, blank=True)
	monday_duration = models.FloatField(default=0)
	tuesday_start = models.TimeField('tuesday start', null=True, blank=True)
	tuesday_end = models.TimeField('tuesday end', null=True, blank=True)
	tuesday_duration = models.FloatField(default=0)
	wednesday_start = models.TimeField('wednesday start', null=True, blank=True)
	wednesday_end = models.TimeField('wednesday end', null=True, blank=True)
	wednesday_duration = models.FloatField(default=0)
	thursday_start = models.TimeField('thursday start', null=True, blank=True)
	thursday_end = models.TimeField('thursday end', null=True, blank=True)
	thursday_duration = models.FloatField(default=0)
	friday_start = models.TimeField('friday start', null=True, blank=True)
	friday_end = models.TimeField('friday end', null=True, blank=True)
	friday_duration = models.FloatField(default=0)
	saturday_start = models.TimeField('saturday start', null=True, blank=True)
	saturday_end = models.TimeField('saturday end', null=True, blank=True)
	saturday_duration = models.FloatField(default=0)
	sunday_start = models.TimeField('sunday start', null=True, blank=True)
	sunday_end = models.TimeField('sunday end', null=True, blank=True)
	sunday_duration = models.FloatField(default=0)
	###Teacher's Skills (identified through skills table)(default=False)
	##ACT
	#English
	skill_1 = models.BooleanField('ACT English', default=False)
	#Math
	skill_2 = models.BooleanField('ACT Math', default=False)
	#Reading
	skill_3 = models.BooleanField('ACT Reading', default=False)
	#Science
	skill_4 = models.BooleanField('ACT Science', default=False)
	#Writing
	skill_5 = models.BooleanField('ACT Writing', default=False)
	##Floor
	#ELA
	skill_6 = models.BooleanField('Floor ELA', default=False)
	#Math
	skill_7 = models.BooleanField('Floor Math', default=False)
	##Subject Tutoring
	#Pre-Calc
	skill_8 = models.BooleanField('Pre-Calculus', default=False)
	#Calc
	skill_9 = models.BooleanField('Calculus', default=False)
	#Biology
	skill_10 = models.BooleanField('Biology', default=False)
	#Chemistry
	skill_11 = models.BooleanField('Chemistry', default=False)
	#Physics
	skill_12 = models.BooleanField('Physics', default=False)
	#Earth/Space
	skill_13 = models.BooleanField('Earth/Space', default=False)
	#History
	skill_14 = models.BooleanField('History', default=False)
	#Spanish
	skill_15 = models.BooleanField('Spanish', default=False)

	def __unicode__(self):
		return self.nickname

	def get_skills(self):
		skills_list = [self.skill_1, self.skill_2, self.skill_3, self.skill_4, self.skill_5, self.skill_6, self.skill_7, self.skill_8, self.skill_9, self.skill_10, self.skill_11, self.skill_12, self.skill_13, self.skill_14, self.skill_15]
		return skills_list

	# def __init__(self, nickname, password, monday_start, monday_end, monday_duration, tuesday_start, tuesday_end, tuesday_duration, wednesday_start, wednesday_end, wednesday_duration, thursday_start, thursday_end, thursday_duration, friday_start, friday_end, friday_duration, saturday_start, saturday_end, saturday_duration, sunday_start, sunday_end, sunday_duration, skill_1, skill_2, skill_3, skill_4, skill_5, skill_6, skill_7, skill_8, skill_9, skill_10, skill_11, skill_12, skill_13, skill_14, skill_15):
	# 	nickname = nickname
	# 	# students_prefer = db.relationship('Student', backref='preferred_teacher', lazy='dynamic')
	# 	password = password
	# 	#Teacher's schedule: available start, availabe end, max duration(default=end-start)
	# 	monday_start = monday_start
	# 	monday_end = monday_end
	# 	monday_duration = monday_duration
	# 	tuesday_start = tuesday_start
	# 	tuesday_end = tuesday_end
	# 	tuesday_duration = tuesday_duration
	# 	wednesday_start = wednesday_start
	# 	wednesday_end = wednesday_end
	# 	wednesday_duration = wednesday_duration
	# 	thursday_start = thursday_start
	# 	thursday_end = thursday_end
	# 	thursday_duration = thursday_duration
	# 	friday_start = friday_start
	# 	friday_end = friday_end
	# 	friday_duration = friday_duration
	# 	saturday_start = saturday_start
	# 	saturday_end = saturday_end
	# 	saturday_duration = saturday_duration
	# 	sunday_start = sunday_start
	# 	sunday_end = sunday_end
	# 	sunday_duration = sunday_duration
	# 	###Teacher's Skills (identified through skills table)(default=False)
	# 	##ACT
	# 	#English
	# 	skill_1 = skill_1
	# 	#Math
	# 	skill_2 = skill_2
	# 	#Reading
	# 	skill_3 = skill_3
	# 	#Science
	# 	skill_4 = skill_4
	# 	#Writing
	# 	skill_5 = skill_5
	# 	##Floor
	# 	#ELA
	# 	skill_6 = skill_6
	# 	#Math
	# 	skill_7 = skill_7
	# 	##Subject Tutoring
	# 	#Pre-Calc
	# 	skill_8 = skill_8
	# 	#Calc
	# 	skill_9 = skill_9
	# 	#Biology
	# 	skill_10 = skill_10
	# 	#Chemistry
	# 	skill_11 = skill_11
	# 	#Physics
	# 	skill_12 = skill_12
	# 	#Earth/Space
	# 	skill_13 = skill_13
	# 	#History
	# 	skill_14 = skill_14
	# 	#Spanish
	# 	skill_15 = skill_15

	# ##user methods
	# @property
	# def is_authenticated(self):
	# 	return True

	# @property
	# def is_active(self):
	#     return True

	# @property
	# def is_anonymous(self):
	#     return False
	# #returns User id
	# def get_id(self):
	# 	try:
	# 		return unicode(self.id) #python 2
	# 	except NameError:
	# 		return str(self.id) #python 3
	# #print user nickname
	# def __repr__(self):
	# 	return '<User %r>' % (self.nickname)

	# @staticmethod
	# def validate_login(password):
	# 	if password == self.password:
	# 		return True
	# 	return False


class Student(models.Model):
	##necessary for creation
	student_id = models.AutoField(primary_key=True)
	student_name = models.CharField(max_length=200, unique=True)
	#Student's requested dates
	# start_date = models.DateField('start date', blank=True)
	start_datetime = models.DateTimeField('start datetime', default=timezone.now)
	end_date = models.DateField('end date', null=True, blank=True)
	scheduled_hours = models.FloatField('scheduled hours', null=True, blank=True)
	#Student's schedule: available start, availabe end, max duration
	monday_start = models.TimeField('monday start', null=True, blank=True)
	monday_end = models.TimeField('monday end', null=True, blank=True)
	monday_duration = models.FloatField(default=0)
	tuesday_start = models.TimeField('tuesday start', null=True, blank=True)
	tuesday_end = models.TimeField('tuesday end', null=True, blank=True)
	tuesday_duration = models.FloatField(default=0)
	wednesday_start = models.TimeField('wednesday start', null=True, blank=True)
	wednesday_end = models.TimeField('wednesday end', null=True, blank=True)
	wednesday_duration = models.FloatField(default=0)
	thursday_start = models.TimeField('thursday start', null=True, blank=True)
	thursday_end = models.TimeField('thursday end', null=True, blank=True)
	thursday_duration = models.FloatField(default=0)
	friday_start = models.TimeField('friday start', null=True, blank=True)
	friday_end = models.TimeField('friday end', null=True, blank=True)
	friday_duration = models.FloatField(default=0)
	saturday_start = models.TimeField('saturday start', null=True, blank=True)
	saturday_end = models.TimeField('saturday end', null=True, blank=True)
	saturday_duration = models.FloatField(default=0)
	sunday_start = models.TimeField('sunday start', null=True, blank=True)
	sunday_end = models.TimeField('sunday end', null=True, blank=True)
	sunday_duration = models.FloatField(default=0)

	#student's preferred teachers
	preferred_teacher1 = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='preferred1', blank=True, null=True)
	preferred_teacher2 = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='preferred2', blank=True, null=True)
	preferred_teacher3 = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='preferred3', blank=True, null=True)

	#student's rejected teachers
	rejected_teacher1 = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='rejected1', blank=True, null=True)
	rejected_teacher2 = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='rejected2', blank=True, null=True)
	rejected_teacher3 = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='rejected3', blank=True, null=True)


	#print student nickname
	def __repr__(self):
		return '<Post %r>' % (self.student_name)

	def __unicode__(self):
		return self.student_name

	def get_skills(self):
		skills_list = [self.skill_1, self.skill_2, self.skill_3, self.skill_4, self.skill_5, self.skill_6, self.skill_7, self.skill_8, self.skill_9, self.skill_10, self.skill_11, self.skill_12, self.skill_13, self.skill_14, self.skill_15]
		return skills_list

class Event(models.Model):
	event_id = models.AutoField(primary_key=True)
	# id=models.IntegerField(default=0)
	start_datetime = models.DateTimeField('Start Date', default=timezone.now)
	duration = models.FloatField(default=0)
	teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, default=-1)
	student = models.ForeignKey(Student, on_delete=models.CASCADE, default=-1)
	notes = models.CharField(max_length=200)

	###Requested Skills (identified through skills table)(default=False)
	##ACT
	#English
	skill_1 = models.BooleanField('ACT English', default=False)
	#Math
	skill_2 = models.BooleanField('ACT Math', default=False)
	#Reading
	skill_3 = models.BooleanField('ACT Reading', default=False)
	#Science
	skill_4 = models.BooleanField('ACT Science', default=False)
	#Writing
	skill_5 = models.BooleanField('ACT Writing', default=False)
	##Floor
	#ELA
	skill_6 = models.BooleanField('Floor ELA', default=False)
	#Math
	skill_7 = models.BooleanField('Floor Math', default=False)
	##Subject Tutoring
	#Pre-Calc
	skill_8 = models.BooleanField('Pre-Calculus', default=False)
	#Calc
	skill_9 = models.BooleanField('Calculus', default=False)
	#Biology
	skill_10 = models.BooleanField('Biology', default=False)
	#Chemistry
	skill_11 = models.BooleanField('Chemistry', default=False)
	#Physics
	skill_12 = models.BooleanField('Physics', default=False)
	#Earth/Space
	skill_13 = models.BooleanField('Earth/Space', default=False)
	#History
	skill_14 = models.BooleanField('History', default=False)
	#Spanish
	skill_15 = models.BooleanField('Spanish', default=False)


	def __repr__(self):
		return '<Event %s, %s, %s>' % (self.teacher, self.student, self.start_datetime)

	def __unicode__(self):
		return 'Teacher: %s, Student: %s, Start: %s' % (self.teacher, self.student, self.start_datetime)
