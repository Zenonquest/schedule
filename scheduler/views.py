from __future__ import print_function
from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponseBadRequest
from django.core.urlresolvers import reverse
from django.views import generic
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status, viewsets, permissions
# from .serializers import TeacherSerializer, StudentSerializer, EventSerializer, SkillSerializer, UserSerializer, GroupSerializer
import oauth2client
from oauth2client import client, tools, file
# from oauth2client.django_orm import Storage
import pdb

# #social auth
# from django.contrib.auth import logout as auth_logout
# from django.contrib.auth.decorators import login_required

# #google calendar api
# import os
# import httplib2
# from oauth2client.contrib import xsrfutil
# from oauth2client.client import flow_from_clientsecrets
# from oauth2client.contrib.django_orm import Storage
# import apiclient
# from apiclient.discovery import build
 
# # from django.contrib.auth.decorators import login_required
# from django.http import HttpResponseBadRequest
# from django.http import HttpResponseRedirect
# from django.shortcuts import render
# from django.conf import settings
# from django.contrib.auth import get_user_model
# from django.core.urlresolvers import reverse

#models.py
from .models import Teacher, Student, Event, Skill #, User, CredentialsModel, FlowModel
# from django.utils import timezone

#other .py files
from scheduler.api import *
from scheduler.gCal import *
from scheduler.login import *
from scheduler.teachers import *
from scheduler.students import *
from scheduler.events import *
from scheduler.availability import *
from scheduler.skills import *

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

#currently non-functional
class EventView(generic.DetailView):
	model = Event
	template_name = 'scheduler/event.html'

class EventIndexView(generic.ListView):
	template_name = 'scheduler/event.html'
	context_object_name = 'events_list'

	def get_queryset(self):
		return Event.objects.order_by('pk')



# @login_required(login_url='/scheduler/login')
# @api_view(['GET'])
# def event_get(request, eventId):
# 	REDIRECT_URI = 'https://www.getpostman.com/oauth2/callback'
# 	# REDIRECT_URI = "https://%s%s" % (
# 	# 	get_current_site(request).domain, reverse("oauth2:return"))
# 	FLOW = flow_from_clientsecrets(
# 		CLIENT_SECRETS,
# 		scope=SCOPES,
# 		redirect_uri=REDIRECT_URI
# 	)
# 	user = request.user
# 	storage = Storage(CredentialsModel, 'id', user, 'credential')
# 	credential = storage.get()
# 	if credential is None or credential.invalid is True:
# 		FLOW.params['state'] = xsrfutil.generate_token(
# 			settings.SECRET_KEY, user)
# 		authorize_url = FLOW.step1_get_authorize_url()
# 		f = FlowModel(id=user, flow=FLOW)
# 		f.save()
# 		return HttpResponseRedirect(authorize_url)
# 	else:
# 		http = httplib2.Http()
# 		http = credential.authorize(http)
# 		service = build('calendar', 'v3', http=http)
# 		try:
# 			event = service.events().get(calendarId='primary', eventId=eventId).execute()
# 		except Event.DoesNotExist:
# 			return HttpResponse(status=404)
# 		return Response(event)

# @login_required(login_url='/scheduler/login')
# @api_view(['GET'])
# def events_get(request):
# 	REDIRECT_URI = 'https://www.getpostman.com/oauth2/callback'
# 	# REDIRECT_URI = "https://%s%s" % (
# 	# 	get_current_site(request).domain, reverse("oauth2:return"))
# 	FLOW = flow_from_clientsecrets(
# 		CLIENT_SECRETS,
# 		scope=SCOPES,
# 		redirect_uri=REDIRECT_URI
# 	)
# 	user = request.user
# 	storage = Storage(CredentialsModel, 'id', user, 'credential')
# 	credential = storage.get()
# 	if credential is None or credential.invalid is True:
# 		FLOW.params['state'] = xsrfutil.generate_token(
# 			settings.SECRET_KEY, user)
# 		authorize_url = FLOW.step1_get_authorize_url()
# 		f = FlowModel(id=user, flow=FLOW)
# 		f.save()
# 		return HttpResponseRedirect(authorize_url)
# 	else:
# 		http = httplib2.Http()
# 		http = credential.authorize(http)
# 		service = build('calendar', 'v3', http=http)
# 		events = service.events().list(calendarId='primary').execute()
# 		return Response(events)

# #add event to google calendar
# def event_post(request):
# 	# REDIRECT_URI = 'http://127.0.0.1:8000/scheduler/oauth2callback'
# 	REDIRECT_URI = 'https://www.getpostman.com/oauth2/callback'
# 	# REDIRECT_URI = "https://%s%s" % (
# 	# 	get_current_site(request).domain, reverse("oauth2:return"))
# 	FLOW = flow_from_clientsecrets(
# 		CLIENT_SECRETS,
# 		scope=SCOPES,
# 		redirect_uri=REDIRECT_URI
# 	)
# 	user = request.user
# 	storage = Storage(CredentialsModel, 'id', user, 'credential')
# 	credential = storage.get()
# 	if credential is None or credential.invalid is True:
# 		FLOW.params['state'] = xsrfutil.generate_token(
# 			settings.SECRET_KEY, user)
# 		authorize_url = FLOW.step1_get_authorize_url()
# 		f = FlowModel(id=user, flow=FLOW)
# 		f.save()
# 		return HttpResponseRedirect(authorize_url)
# 	else:
		
# 		http = httplib2.Http()
# 		http = credential.authorize(http)
# 		service = build('calendar', 'v3', http=http)
# 		data = request.data
# 		event = {
# 			'location': '5127 Sheridan Blvd, Broomfield, CO 80020',
# 			'start': {
# 				'timeZone': 'America/Denver',
# 			},
# 			'end' : {
# 				'timeZone': 'America/Denver',
# 			},
# 		}
# 		if 'event_id' in data:
# 			event['summary']= 'Event' + data['event_id']
# 		else:
# 			event['summary']= 'Event w/o ID'
# 		if 'description' in data:
# 			event['description']= data['description']
# 		else:
# 			event['summary']= 'Test for event w/o ID'

# 		#MANDATORY ARGUMENT
# 		if 'start_datetime' in data:
# 			event['start']['dateTime']= data['start_datetime']
# 		else:
# 			event['start']['dateTime']= '2016-05-28T13:00:00-07:00'
# 		#MANDATORY ARGUMENT
# 		if 'end_datetime' in data:
# 			event['end']['dateTime']= data['end_datetime']
# 		else:
# 			event['end']['dateTime']= '2016-05-28T14:00:00-07:00'

# 		if 'recurrence' in data:
# 			event['recurrence'] = data['recurrence']
# 		else:
# 			event['recurrence'] ='RRULE:FREQ=DAILY;COUNT=2'

# 		if 'reminders' in data:
# 			event['reminders']= data['reminders']
# 		else:
# 			event['reminders']= {
# 				'useDefault': False,
# 				'overrides': [
# 					{'method': 'email', 'minutes': 24 * 60},
# 					{'method': 'popup', 'minutes': 10},
# 				],
# 			}	

# 		e = service.events().insert(calendarId='primary', body=event).execute()
# 		return HttpResponseRedirect("/scheduler/home")


# #GET: return all skills lists
# #POST: add one skill list, request must be dictionary w ALL skills (skills{'skill_1: True, 'skill_2':False..., 'skill_15:True'})
# @api_view(['GET', 'POST'])
# def skill_collection(request):
# 	if request.method == 'GET':
# 		skills = Skill.objects.all()
# 		serializer = SkillSerializer(skills, many=True)
# 		return Response(serializer.data)
# 	if request.method == 'POST':
# 		data = request.data
# 		serializer = SkillSerializer(data=data, partial=True)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data, status=status.HTTP_201_CREATED)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# 	return HttpResponse('I\'m a teapot short and stout.', status=418)


# #GET: return all skills lists
# #POST: edit one skill list, request must be dictionary w ALL skills (skills{'skill_1: True, 'skill_2':False..., 'skill_15:True'})
# @api_view(['GET', 'POST'])
# def skill_element(request, pk):
# 	try:
# 		skill = Skill.objects.get(pk=pk)
# 	except Teacher.DoesNotExist:
# 		return HttpResponse(status=404)
		
# 	if request.method == 'GET':
# 		serializer = SkillSerializer(skill)
# 		return Response(serializer.data)

# 	if request.method == 'POST':
# 		data = request.data
# 		serializer =SkillSerializer(skill, data=data, partial=True)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data, status=status.HTTP_201_CREATED)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# 	return HttpResponse('I\'m a teapot short and stout.', status=418)


# #GET: return all skills lists
# #POST: add one skill list, request must be dictionary w ALL availability (availability{'skill_1: True, 'skill_2':False..., 'skill_15:True'})
# @api_view(['GET', 'POST'])
# def availability_collection(request):
# 	if request.method == 'GET':
# 		availability = Skill.objects.all()
# 		serializer = SkillSerializer(availability, many=True)
# 		return Response(serializer.data)
# 	if request.method == 'POST':
# 		data = request.data
# 		serializer = SkillSerializer(data=data, partial=True)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data, status=status.HTTP_201_CREATED)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# 	return HttpResponse('I\'m a teapot short and stout.', status=418)


# #GET: return all availability lists
# #POST: edit one skill list, request must be dictionary w ALL availability (availability{'skill_1: True, 'skill_2':False..., 'skill_15:True'})
# @api_view(['GET', 'POST'])
# def availability_element(request, pk):
# 	try:
# 		skill = Skill.objects.get(pk=pk)
# 	except Teacher.DoesNotExist:
# 		return HttpResponse(status=404)
		
# 	if request.method == 'GET':
# 		serializer = SkillSerializer(skill)
# 		return Response(serializer.data)

# 	if request.method == 'POST':
# 		data = request.data
# 		serializer =SkillSerializer(skill, data=data, partial=True)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data, status=status.HTTP_201_CREATED)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# 	return HttpResponse('I\'m a teapot short and stout.', status=418)

# ###TESTING OAUTH2
# def login(request):
# 	# context = RequestContext(request, {
# 	#     'request': request, 'user': request.user})
# 	# return render_to_response('login.html', context_instance=context)
# 	return render(request, 'scheduler/login.html')


# @login_required(login_url='/')
# def home(request):
# 	return render_to_response('scheduler/home.html')


# def logout(request):
# 	auth_logout(request)
# 	return redirect('/scheduler')

# #google calendar api
# def get_credentials():
# 	"""Gets valid user credentials from storage.
	
# 	If nothing has been stored, or if the stored credentials are invalid,
# 	the OAuth2 flow is completed to obtain the new credentials.

# 	Returns:
# 	    Credentials, the obtained credential.
# 	"""
# 	home_dir = os.path.expanduser('~')
# 	credential_dir = os.path.join(home_dir, '.credentials')
# 	if not os.path.exists(credential_dir):
# 		os.makedirs(credential_dir)
# 	redential_path = os.path.join(credential_dir,
# 								'scheduler.json')

# 	store = oauth2client.file.Storage(credential_path)
# 	credentials = store.get()
# 	if not credentials or credentials.invalid:
# 		flow = client.flow_from_clientsecrets(CLIENT_SECRET, SCOPES)
# 		flow.user_agent = APPLICATION_NAME
# 		if flags:
# 			credentials = tools.run_flow(flow, store, flags)
# 		else: # Needed only for compatibility with Python 2.6
# 			credentials = tools.run(flow, store)
# 		print('Storing credentials to ' + credential_path)
# 	return credentials

# @login_required(login_url='login/')
# def index(request):
# 	# use the first REDIRECT_URI if you are developing your app
# 	# locally, and the second in production
# 	REDIRECT_URI = 'http://127.0.0.1:8000/scheduler/oauth2callback'
# 	# REDIRECT_URI = "https://%s%s" % (
# 	# 	get_current_site(request).domain, reverse("oauth2:return"))
# 	FLOW = flow_from_clientsecrets(
# 		CLIENT_SECRETS,
# 		scope=SCOPES,
# 		redirect_uri=REDIRECT_URI
# 	)
# 	user = request.user
# 	storage = Storage(CredentialsModel, 'id', user, 'credential')
# 	credential = storage.get()
# 	if credential is None or credential.invalid is True:
# 		FLOW.params['state'] = xsrfutil.generate_token(
# 			settings.SECRET_KEY, user)
# 		authorize_url = FLOW.step1_get_authorize_url()
# 		f = FlowModel(id=user, flow=FLOW)
# 		f.save()
# 		return HttpResponseRedirect(authorize_url)
# 	else:
# 		http = httplib2.Http()
# 		http = credential.authorize(http)
# 		service = build('calendar', 'v3', http=http)
# 		event = {
# 			'summary': 'Event Check',
# 			'location': '5127 Sheridan Blvd, Broomfield, CO 80020',
# 			'description': 'Test for event 1',
# 			'start': {
# 				'dateTime': '2016-05-28T09:00:00-07:00',
# 				'timeZone': 'America/Denver',
# 			},
# 			'end' : {
# 				'dateTime': '2016-05-28T13:00:00-07:00',
# 				'timeZone': 'America/Denver',
# 			},
# 			'recurrence': [
# 				'RRULE:FREQ=DAILY;COUNT=2'
# 			],
# 			'reminders': {
# 				'useDefault': False,
# 				'overrides': [
# 					{'method': 'email', 'minutes': 24 * 60},
# 					{'method': 'popup', 'minutes': 10},
# 				],
# 			},
# 		}

# 		e = service.events().insert(calendarId='primary', body=event).execute()

# 		return HttpResponseRedirect("/scheduler/home")

		# return ('''*** %r event added:
		# 	Start: %s
		# 	End: $s''' (e['summary'].encode('utf-8'),
		# 		e['start']['dateTime'], e['end']['dateTime']))
		# # return render(
		# 	request, 'oauth2_authentication/main.html', {'ids':ids})


