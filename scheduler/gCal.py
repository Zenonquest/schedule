from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, viewsets, permissions

from django.contrib.auth.decorators import login_required

from .models import CredentialsModel, FlowModel

#google calendar api
import os
import httplib2
from oauth2client.contrib import xsrfutil
from oauth2client.client import flow_from_clientsecrets
from oauth2client.contrib.django_orm import Storage
# import apiclient
from apiclient.discovery import build
 
from django.contrib.auth.decorators import login_required

from django.http import HttpResponseBadRequest
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
import pdb
from .models import CredentialsModel
# from django.contrib.sites.models import get_current_site
from django.template import *

import json

CLIENT_SECRETS = os.path.join(
	os.path.dirname(__file__), 'client_secret.json')
# cs = str(ClientSecret.objects.get(pk=1))
# CLIENT_SECRETS = json.dumps({
# 	"web":{
# 		"client_id":"323423619559-orlpuuiaalb7sp3ooblt4mjmp32ffq1t.apps.googleusercontent.com",
# 		"project_id":"psyched-oxide-115203",
# 		"auth_uri":"https://accounts.google.com/o/oauth2/auth",
# 		"token_uri":"https://accounts.google.com/o/oauth2/token",
# 		# "client_secret":os.environ['CLIENT_SECRET'],
# 		"client_secret": cs,
# 		"redirect_uris":[
# 			"http://127.0.0.1:8000/scheduler/complete/google-oauth2/",
# 			"http://127.0.0.1:8000/scheduler/oauth2callback"
# 		],
# 		"javascript_origins":["http://localhost:8000"]
# 	}
# }, ensure_ascii=False)

# REDIRECT_URI = 'http://127.0.0.1:8000/scheduler/oauth2callback'
# REDIRECT_URI = "https://%s%s" % (
# 	get_current_site(request).domain, reverse("scheduler:return"))


SCOPES = (
	'https://www.googleapis.com/auth/calendar',
	'https://www.googleapis.com/auth/drive.metadata.readonly'
)
# REDIRECT_URI = "https://%s%s" % (
# 	request.get_host, reverse("scheduler:return"))
# FLOW = flow_from_clientsecrets(
# 		CLIENT_SECRETS,
# 		scope=SCOPES,
# 		redirect_uri=REDIRECT_URI
# 	)

@login_required
@api_view(['GET'])
def event_get(request, eventId):
	REDIRECT_URI = "https://%s%s" % (
		request.get_host, reverse("scheduler:return"))
	FLOW = flow_from_clientsecrets(
			CLIENT_SECRETS,
			scope=SCOPES,
			redirect_uri=REDIRECT_URI
		)

	user = request.user
	storage = Storage(CredentialsModel, 'id', user, 'credential')
	credential = storage.get()
	if credential is None or credential.invalid is True:
		FLOW.params['state'] = xsrfutil.generate_token(
			settings.SECRET_KEY, user)
		authorize_url = FLOW.step1_get_authorize_url()
		f = FlowModel(id=user, flow=FLOW)
		f.save()
		return HttpResponseRedirect(authorize_url)
	else:
		http = httplib2.Http()
		http = credential.authorize(http)
		service = build('calendar', 'v3', http=http)
		try:
			event = service.events().get(calendarId='primary', eventId=eventId).execute()
		except Event.DoesNotExist:
			return HttpResponse(status=404)
		return Response(event)

@login_required
@api_view(['GET'])
def events_get(request):
	REDIRECT_URI = "https://%s%s" % (
		request.get_host, reverse("scheduler:return"))
	FLOW = flow_from_clientsecrets(
			CLIENT_SECRETS,
			scope=SCOPES,
			redirect_uri=REDIRECT_URI
		)
	user = request.user
	storage = Storage(CredentialsModel, 'id', user, 'credential')
	credential = storage.get()
	if credential is None or credential.invalid is True:
		FLOW.params['state'] = xsrfutil.generate_token(
			settings.SECRET_KEY, user)
		authorize_url = FLOW.step1_get_authorize_url()
		f = FlowModel(id=user, flow=FLOW)
		f.save()
		return HttpResponseRedirect(authorize_url)
	else:
		http = httplib2.Http()
		http = credential.authorize(http)
		service = build('calendar', 'v3', http=http)
		events = service.events().list(calendarId='primary').execute()
		return Response(events)

#add event to google calendar
def event_post(request):
	REDIRECT_URI = "https://%s%s" % (
		request.get_host, reverse("scheduler:return"))
	FLOW = flow_from_clientsecrets(
			CLIENT_SECRETS,
			scope=SCOPES,
			redirect_uri=REDIRECT_URI
		)

	user = request.user
	storage = Storage(CredentialsModel, 'id', user, 'credential')
	credential = storage.get()
	if credential is None or credential.invalid is True:
		FLOW.params['state'] = xsrfutil.generate_token(
			settings.SECRET_KEY, user)
		authorize_url = FLOW.step1_get_authorize_url()
		f = FlowModel(id=user, flow=FLOW)
		f.save()
		return HttpResponseRedirect(authorize_url)
	else:
		
		http = httplib2.Http()
		http = credential.authorize(http)
		service = build('calendar', 'v3', http=http)
		data = request.data
		event = {
			'location': '5127 Sheridan Blvd, Broomfield, CO 80020',
			'start': {
				'timeZone': 'America/Denver',
			},
			'end' : {
				'timeZone': 'America/Denver',
			},
		}
		if 'event_id' in data:
			event['summary']= 'Event' + data['event_id']
		else:
			event['summary']= 'Event w/o ID'
		if 'description' in data:
			event['description']= data['description']
		else:
			event['summary']= 'Test for event w/o ID'

		#MANDATORY ARGUMENT
		if 'start_datetime' in data:
			event['start']['dateTime']= data['start_datetime']
		else:
			event['start']['dateTime']='2016-05-28T20:00:00-07:00'
		#MANDATORY ARGUMENT
		if 'end_datetime' in data:
			event['end']['dateTime']= data['end_datetime']
		else:
			event['end']['dateTime']= '2016-05-28T21:00:00-07:00'#str(datetime.datetime.now() + datetime.timedelta(hours=1))#str(timezone.now() +timezone.timedelta(hours=1))#'2016-05-28T14:00:00-07:00'

		if 'recurrence' in data:
			event['recurrence'] = data['recurrence']
		else:
			event['recurrence'] ='RRULE:FREQ=DAILY;COUNT=2'

		if 'reminders' in data:
			event['reminders']= data['reminders']
		else:
			event['reminders']= {
				'useDefault': False,
				'overrides': [
					{'method': 'email', 'minutes': 24 * 60},
					{'method': 'popup', 'minutes': 10},
				],
			}	

		e = service.events().insert(calendarId='primary', body=event).execute()

