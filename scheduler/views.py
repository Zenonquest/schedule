from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, viewsets, permissions
from .serializers import TeacherSerializer, StudentSerializer, EventSerializer, SkillSerializer, UserSerializer, GroupSerializer
from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope, TokenHasScope

from .models import Teacher, Student, Event, Skill
from django.contrib.auth.models import User, Group

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

#GET: return all teachers
#POST: creates teacher (body needs nickname)
@api_view(['GET', 'POST'])
def teacher_collection(request):
	if request.method == 'GET':
		teachers = Teacher.objects.all()
		serializer = TeacherSerializer(teachers, many=True)
		return Response(serializer.data)
	
	if request.method == 'POST':
		data = {'nickname': request.data.get("nickname")}
		serializer = TeacherSerializer(data=data, partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	return HttpResponse('I\'m a teapot short and stout.', status=418)
		
#GET: return one teacher
#POST: edit one teacher
#editable fields: all
@api_view(['GET', 'POST'])
def teacher_element(request, pk):
	#collect single teacher before processing request
	try:
		teacher = Teacher.objects.get(pk=pk)
	except Teacher.DoesNotExist:
		return HttpResponse(status=404)
		
	if request.method == 'GET':
		serializer = TeacherSerializer(teacher)
		return Response(serializer.data)

	if request.method == 'POST':
		data = request.data
		serializer = TeacherSerializer(teacher, data=data, partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	return HttpResponse('I\'m a teapot short and stout.', status=418)

#GET: return all students
#POST: create student (body needs student_name)
@api_view(['GET', 'POST'])
def student_collection(request):
	if request.method == 'GET':
		students = Student.objects.all()
		serializer = StudentSerializer(students, many=True)
		return Response(serializer.data)
	
	if request.method == 'POST':
		data = request.data
		serializer = StudentSerializer(data=data, partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	return HttpResponse('I\'m a teapot short and stout.', status=418)

#return all students
#edit student. all fields available
@api_view(['GET', 'POST'])
def student_element(request, pk):
	try:
		student = Student.objects.get(pk=pk)
	except Student.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializer = StudentSerializer(student)
		return Response(serializer.data)

	if request.method == 'POST':
		data = request.data
		serializer = StudentSerializer(student, data=data, partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	return HttpResponse('I\'m a teapot short and stout.', status=418)

#GET: return all events
#POST: add new event
##post request requires: student_id, teacher_id, start_datetime, end_datetime
@api_view(['GET','POST'])
def event_collection(request):
	if request.method == 'GET':
		events = Event.objects.all()
		serializer = EventSerializer(events, many=True)
		return Response(serializer.data)
	if request.method == 'POST':
		data = {'student':request.data.get("student_id"), 'teacher':request.data.get("teacher_id")}
		serializer = EventSerializer(data=data, partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	return HttpResponse('I\'m a teapot short and stout.', status=418)

#GET: return one event
#POST: edit one event's skills, skills{'skill_1: True, 'skill_2':False...}
@api_view(['GET','POST'])
def event_element(request, pk):
	try:
		event = Event.objects.get(pk=pk)
	except Event.DoesNotExist:
		return HttpResponse(status=404)
	if request.method == 'GET':
		event = Event.objects.get(pk=pk)
		serializer = EventSerializer(event)
		return Response(serializer.data)
	if request.method == 'POST':
		data = request.data
		serializer = EventSerializer(event, data=data, partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	return HttpResponse('I\'m a teapot short and stout.', status=418)


#GET: return all skills lists
#POST: add one skill list, request must be dictionary w ALL skills (skills{'skill_1: True, 'skill_2':False..., 'skill_15:True'})
@api_view(['GET', 'POST'])
def skill_collection(request):
	if request.method == 'GET':
		skills = Skill.objects.all()
		serializer = SkillSerializer(skills, many=True)
		return Response(serializer.data)
	if request.method == 'POST':
		data = request.data
		serializer = SkillSerializer(data=data, partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	return HttpResponse('I\'m a teapot short and stout.', status=418)


#GET: return all skills lists
#POST: edit one skill list, request must be dictionary w ALL skills (skills{'skill_1: True, 'skill_2':False..., 'skill_15:True'})
@api_view(['GET', 'POST'])
def skill_element(request, pk):
	try:
		skill = Skill.objects.get(pk=pk)
	except Teacher.DoesNotExist:
		return HttpResponse(status=404)
		
	if request.method == 'GET':
		serializer = SkillSerializer(skill)
		return Response(serializer.data)

	if request.method == 'POST':
		data = request.data
		serializer =SkillSerializer(skill, data=data, partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	return HttpResponse('I\'m a teapot short and stout.', status=418)


##oauth2
# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ['groups']
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


