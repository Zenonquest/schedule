from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import TeacherSerializer, EventSerializer


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
		return Event.objects.order_by('pk')[:3]


@api_view(['GET'])
def teacher_collection(request):
	if request.method == 'GET':
		teachers = Teacher.objects.all()
		serializer = TeacherSerializer(teachers, many=True)
		return Response(serializer.data)

@api_view(['GET'])
def teacher_element(request, pk):
	try:
		teacher = Teacher.objects.get(pk=pk)
	except Teacher.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializer = TeacherSerializer(teacher)
		return Response(serializer.data)


@api_view(['GET','POST'])
def event_collection(request):
	if request.method == 'GET':
		event = Event.objects.all()
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


@api_view(['POST'])
def event_element(request, pk):
	if request.method == 'POST':
		teachers = Teacher.objects.all()
		student = Student.objects.get(pk=pk)
		student_skills = student.get_skills()
		for teacher in teachers:
			teacher_skills = teacher.get_skills()
			if student.monday_start < teacher.monday_start:
				continue
			if student.monday_end > teacher.monday_end:
				continue
			for idx, skill in enumerate(student_skills):
				if skill == False:
					continue
				if teachers_skill[idx] == False:
					break
				data = {'student':student.student_id, 'teacher':teacher.id, 'start_datetime':student.monday_start, 'duration':student.monday_duration, 'notes':"test note"}
				#use serializer to add row to event table
				serializer = EventSerializer(data=data)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)