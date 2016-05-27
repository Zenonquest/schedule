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
import apiclient
from apiclient.discovery import build
 
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse

from .models import CredentialsModel, ClientSecret

import json
###WEB Client Secrets
##Client_secrets = db.get..
CLIENT_SECRETS = json.dumps({
	"web":{
		"client_id":"323423619559-orlpuuiaalb7sp3ooblt4mjmp32ffq1t.apps.googleusercontent.com",
		"project_id":"psyched-oxide-115203",
		"auth_uri":"https://accounts.google.com/o/oauth2/auth",
		"token_uri":"https://accounts.google.com/o/oauth2/token",
		"auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs",
		# "client_secret":os.environ['CLIENT_SECRET'],
		# "client_secret": ClientsecreT.objects.get(pk=1),
		"redirect_uris":[
			"http://127.0.0.1:8000/scheduler/complete/google-oauth2/",
			"http://127.0.0.1:8000/scheduler/oauth2callback"
		],
		"javascript_origins":["http://localhost:8000"]
	}
})
# client_dict = {
# 	"client_id" : os.environ['client_id'],
# 	"project_id" : os.environ['project_id'],
# 	"auth_uri" : os.environ['']
# }

###LOCAL Client Secrets
# CLIENT_SECRETS = os.path.join(
# 	os.path.dirname(__file__), 'client_secret.json')

SCOPES = (
	'https://www.googleapis.com/auth/calendar',
	'https://www.googleapis.com/auth/drive.metadata.readonly'
)

@login_required(login_url='/scheduler/login')
@api_view(['GET'])
def event_get(request, eventId):
	# REDIRECT_URI = 'https://www.getpostman.com/oauth2/callback'
	REDIRECT_URI = "https://%s%s" % (
		get_current_site(request).domain, reverse("scheduler:return"))
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

@login_required(login_url='/scheduler/login')
@api_view(['GET'])
def events_get(request):
	# REDIRECT_URI = 'https://www.getpostman.com/oauth2/callback'
	REDIRECT_URI = "https://%s%s" % (
		get_current_site(request).domain, reverse("scheduler:return"))
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
	# REDIRECT_URI = 'http://127.0.0.1:8000/scheduler/oauth2callback'
	# REDIRECT_URI = 'https://www.getpostman.com/oauth2/callback'
	REDIRECT_URI = "https://%s%s" % (
		get_current_site(request).domain, reverse("scheduler:return"))
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
			event['start']['dateTime']= '2016-05-28T13:00:00-07:00'
		#MANDATORY ARGUMENT
		if 'end_datetime' in data:
			event['end']['dateTime']= data['end_datetime']
		else:
			event['end']['dateTime']= '2016-05-28T14:00:00-07:00'

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
		return HttpResponseRedirect("/scheduler/home")


def get_credentials():
	"""Gets valid user credentials from storage.
	
	If nothing has been stored, or if the stored credentials are invalid,
	the OAuth2 flow is completed to obtain the new credentials.

	Returns:
	    Credentials, the obtained credential.
	"""
	home_dir = os.path.expanduser('~')
	credential_dir = os.path.join(home_dir, '.credentials')
	if not os.path.exists(credential_dir):
		os.makedirs(credential_dir)
	redential_path = os.path.join(credential_dir,
								'scheduler.json')

	store = oauth2client.file.Storage(credential_path)
	credentials = store.get()
	if not credentials or credentials.invalid:
		flow = client.flow_from_clientsecrets(CLIENT_SECRET, SCOPES)
		flow.user_agent = APPLICATION_NAME
		if flags:
			credentials = tools.run_flow(flow, store, flags)
		else: # Needed only for compatibility with Python 2.6
			credentials = tools.run(flow, store)
		print('Storing credentials to ' + credential_path)
	return credentials


@login_required
def auth_return(request):
	user = request.user
	if not xsrfutil.validate_token(
		settings.SECRET_KEY, request.GET['state'], user):
		return HttpResponseBadRequest()
	FLOW = FlowModel.objects.get(id=user).flow
	credential = FLOW.step2_exchange(request.GET)
	storage = Storage(CredentialsModel, 'id', user, 'credential')
	storage.put(credential)
	return HttpResponseRedirect("/scheduler")