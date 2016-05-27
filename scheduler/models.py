from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# import oauth2client
from oauth2client.contrib.django_orm import FlowField, CredentialsField
import datetime


# Create your models here.
class Teacher(models.Model):
	teacher_id = models.AutoField(primary_key=True)
	nickname = models.CharField(max_length=200, unique=True)

	def __unicode__(self):
		return self.nickname

	def get_skills(self):
		skills_list = [self.skill_1, self.skill_2, self.skill_3, self.skill_4, self.skill_5, self.skill_6, self.skill_7, self.skill_8, self.skill_9, self.skill_10, self.skill_11, self.skill_12, self.skill_13, self.skill_14, self.skill_15]
		return skills_list


class Student(models.Model):
	##necessary for creation
	student_id = models.AutoField(primary_key=True)
	student_name = models.CharField(max_length=200, unique=True)

	#student's preferred teachers
	preferred_teacher1 = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='preferred1', blank=True, null=True)
	preferred_teacher2 = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='preferred2', blank=True, null=True)
	preferred_teacher3 = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='preferred3', blank=True, null=True)

	#student's rejected teachers
	rejected_teacher1 = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='rejected1', blank=True, null=True)
	rejected_teacher2 = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='rejected2', blank=True, null=True)
	rejected_teacher3 = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='rejected3', blank=True, null=True)

	#Student's requested dates
	# start_date = models.DateField('start date', blank=True)
	# start_datetime = models.DateTimeField('start datetime', default=timezone.now)
	# end_date = models.DateField('end date', null=True, blank=True)
	# scheduled_hours = models.FloatField('scheduled hours', null=True, blank=True)
	#Student's schedule: available start, availabe end, max duration

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
	start_datetime = models.DateTimeField('Start Date', default=timezone.now)
	end_datetime = models.DateTimeField('End Date', default=timezone.now)
	duration = models.FloatField(default=0)
	teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, default=-1)
	student = models.ForeignKey(Student, on_delete=models.CASCADE, default=-1)
	notes = models.CharField(max_length=200)


	def __repr__(self):
		return '<Event %s, %s, %s>' % (self.teacher, self.student, self.start_datetime)

	def __unicode__(self):
		return 'Teacher: %s, Student: %s, Start: %s' % (self.teacher, self.student, self.start_datetime)



#skills table. choose either teacher or event for foreign key
class Skill(models.Model):
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

	event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True, blank=True)
	teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True, blank=True)	

	def skillsArray(self):
		skills = [self.skill_1, self.skill_2, self.skill_3, self.skill_4, self.skill_5, self.skill_6, self.skill_7, self.skill_8, self.skill_9, 
			self.skill_10, self.skill_11, self.skill_12, self.skill_13, self.skill_14, self.skill_15]
		return skills

	def __unicode__(self):
		return 'Skills: %s' (self.skillsArray())

class Availability(models.Model):
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

	teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

class FlowModel(models.Model):
	id = models.ForeignKey(User, primary_key=True)
	flow = FlowField()

class CredentialsModel(models.Model):
	id = models.ForeignKey(User, primary_key=True)
	credential = CredentialsField()

class ClientSecret(models.Model):
	key = models.CharField(max_length=200)

# class Dicty(models.Model):
# 	name = models.CharField(max_length=50)

# class KeyVal(models.Model):
# 	container = models.ForeignKey(Dicty, db_index=True)
# 	key = models.CharField(max_length=240, db_index=True)
# 	value = models.CharField(max_length=240, db_index=True)