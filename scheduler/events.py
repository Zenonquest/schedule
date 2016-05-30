from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, viewsets, permissions

from django.contrib.auth.decorators import login_required

from .models import Event

from .gCal import *

from .serializers import EventSerializer

#GET: return all events
#POST: add new event
##post request requires: student_id, teacher_id, start_datetime, end_datetime
@login_required
@api_view(['GET','POST'])
def event_collection(request):
	if request.method == 'GET':
		events = Event.objects.all()
		serializer = EventSerializer(events, many=True)
		return Response(serializer.data)
	if request.method == 'POST':
		event_info = request.data
		data = {'student':request.data.get("student_id"), 'teacher':request.data.get("teacher_id")}
		serializer = EventSerializer(data=data, partial=True)
		if serializer.is_valid():
			event_post(request) #sends data to create event in gCal
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

