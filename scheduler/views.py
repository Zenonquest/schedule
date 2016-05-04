from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import TeacherSerializer, StudentSerializer, EventSerializer


from .models import Teacher, Student, Event


class IndexView(generic.ListView):
	template_name = 'scheduler/index.html'
	context_object_name = 'teachers_list'

	def get_queryset(self):
		return Teacher.objects.order_by('nickname')[:3]

class StudentView(generic.DetailView):
	model = Student
	template_name = 'scheduler/student.html'

class TeacherView(generic.DetailView):
	model = Teacher
	context_object_name = 'teacher'
	template_name = 'scheduler/teacher.html'

class EventView(generic.DetailView):
	model = Event
	template_name = 'scheduler/event.html'

class EventIndexView(generic.ListView):
	template_name = 'scheduler/event.html'
	context_object_name = 'events_list'

	def get_queryset(self):
		return Event.objects.order_by('pk')

#return all teachers
#POST: edit all teachers (only monday_duration)
@api_view(['GET', 'POST'])
def teacher_collection(request):
	if request.method == 'GET':
		teachers = Teacher.objects.all()
		serializer = TeacherSerializer(teachers, many=True)
		return Response(serializer.data)
	if request.method == 'POST':
		data = request.data
		teachers = Teacher.objects.all()
		for teacher in teachers:
			data = request.data.get('monday_duration')
			serializer = TeacherSerializer(teacher, data=data, partial=True)
			if serializer.is_valid():
				serializer.save()
		updated_teachers = Teacher.objects.all()
		serializer = TeacherSerializer(teachers, many=True)
		return Response(serializer.data)

#return one teacher
#POST: edit one teacher
@api_view(['GET', 'POST'])
def teacher_element(request, pk):
	try:
		teacher = Teacher.objects.get(pk=pk)
	except Teacher.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializer = TeacherSerializer(teacher)
		return Response(serializer.data)

	if request.method == 'POST':
		data = {'monday_duration': request.data.get('monday_duration')}
		serializer = TeacherSerializer(teacher, data=data, partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return HttpResponse('I\'m a teapot short and stout.', status=418)

#return all students
@api_view(['GET'])
def student_collection(request):
	if request.method == 'GET':
		students = Student.objects.all()
		serializer = StudentSerializer(students, many=True)
		return Response(serializer.data)

#return all students
@api_view(['GET'])
def student_element(request, pk):
	try:
		student = Student.objects.get(pk=pk)
	except Student.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializer = StudentSerializer(student)
		return Response(serializer.data)

#GET: return all events
#POST: add new event
@api_view(['GET','POST'])
def event_collection(request):
	if request.method == 'GET':
		events = Event.objects.all()
		serializer = EventSerializer(events, many=True)
		return Response(serializer.data)
	if request.method == 'POST':
		teachers = Teacher.objects.all()
		student = Student.objects.get(pk=1)
		for teacher in teachers:
			if student.monday_start < teacher.monday_end:
				data = {'student':student.student_id, 'teacher':teacher.id, 'start_datetime':student.monday_start, 'duration':student.monday_duration, 'notes':"test note"}
				serializer = EventSerializer(data=data)
				if serializer.is_valid():
					serializer.save()
					return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#GET: return one event
#POST: edit one event
@api_view(['GET','POST'])
def event_element(request, pk):
	if request.method == 'GET':
		event = Event.objects.get(pk=pk)
		serializer = EventSerializer(event)
		return Response(serializer.data)
	if request.method == 'POST':
		teachers = Teacher.objects.all()
		student = Student.objects.get(pk=pk)
		student_skills = student.get_skills()
		for teacher in teachers:
			teacher_skills = teacher.get_skills()
			#check monday match
			if student.monday_start: 
				if teacher.monday_start:
					if student.monday_start < teacher.monday_start:
						continue;
				else: 
					continue;
			if student.monday_end: 
				if teacher.monday_end:
					if student.monday_end > teacher.monday_end:
						continue
				else:
					continue;
			#check tuesday match
			if student.tuesday_start: 
				if teacher.tuesday_start:
					if student.tuesday_start < teacher.tuesday_start:
						continue
				else:
					continue;
			if student.tuesday_end: 
				if teacher.tuesday_end:
					if student.tuesday_end > teacher.tuesday_end:
						continue
				else:
					continue;
			#check wednesday match
			if student.wednesday_start: 
				if teacher.wednesday_start:
					if student.wednesday_start < teacher.wednesday_start:
						continue
				else:
					continue;
			if student.wednesday_end: 
				if teacher.wednesday_end:
					if student.wednesday_end > teacher.wednesday_end:
						continue
				else:
					continue;
			#check thursday match
			if student.thursday_start: 
				if teacher.thursday_start:
					if student.thursday_start < teacher.thursday_start:
						continue
				else:
					continue
			if student.thursday_end: 
				if teacher.thursday_end:
					if student.thursday_end > teacher.thursday_end:
						continue
				else:
					continue
			#check friday match
			if student.friday_start: 
				if teacher.friday_start:
					if student.friday_start < teacher.friday_start:
						continue
				else:
					continue
						
			if student.friday_end: 
				if teacher.friday_end:
					if student.friday_end > teacher.friday_end:
						continue
				else:
					continue

			#check saturday match
			if student.saturday_start: 
				if teacher.saturday_start:
					if student.saturday_start < teacher.saturday_start:
						continue
				else:
					continue
						
			if student.saturday_end: 
				if teacher.saturday_end:
					if student.saturday_end > teacher.saturday_end:
						continue
				else:
					continue

			#check sunday match
			if student.sunday_start: 
				if teacher.sunday_start:
					if student.sunday_start < teacher.sunday_start:
						continue
				else:
					continue
						
			if student.sunday_end: 
				if teacher.sunday_end:
					if student.sunday_end > teacher.sunday_end:
						continue
				else:
					continue
			#check for skills match												
			for idx, skill in enumerate(student_skills):
				if skill == False:
					continue
				if teacher_skills[idx] == False:
					break

			#if schedule match and skills match then create event.
			data = {'student':student.student_id, 'teacher':teacher.teacher_id, 'start_datetime':student.start_datetime, 'duration':student.monday_duration, 'notes':"test note"}
			#use serializer to add row to event table
			serializer = EventSerializer(data=data)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data, status=status.HTTP_201_CREATED)
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		return HttpResponse('I\'m a teapot short and stout.', status=418)