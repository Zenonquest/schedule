

##views.py
# @login_required
# def auth_return(request):
# 	user = request.user
# 	if not xsrfutil.validate_token(
# 		settings.SECRET_KEY, str(request.GET['state']), user):
# 		return HttpResponseBadRequest()
# 	FLOW = FlowModel.objects.get(id=user).flow
# 	credential = FLOW.step2_exchange(request.GET)
# 	storage = Storage(CredentialsModel, 'id', user, 'credential')
# 	storage.put(credential)
# 	return HttpResponseRedirect("/scheduler/home")







###LOCAL Client Secrets
# /schedule2/scheduler/<file>
# CLIENT_SECRETS = os.path.join(
# 	os.path.dirname(__file__), 'client_secret.json')

# cs = str(ClientSecret.objects.get(pk=1))

# CLIENT_SECRETS = {
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
# # }

# REDIRECT_URI = 'http://127.0.0.1:8000/scheduler/oauth2callback'

# SCOPES = (
# 	'https://www.googleapis.com/auth/calendar',
# 	'https://www.googleapis.com/auth/drive.metadata.readonly'
# )
# # REDIRECT_URI = "https://%s%s" % (
# # 	get_current_site(request).domain, reverse("scheduler:return"))
# FLOW = flow_from_clientsecrets(
# 		CLIENT_SECRETS,
# 		scope=SCOPES,
# 		redirect_uri=REDIRECT_URI
# 	)

# @login_required
# @api_view(['GET'])
# def event_get(request, eventId):
# 	# REDIRECT_URI = 'https://www.getpostman.com/oauth2/callback'
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

# @login_required
# @api_view(['GET'])
# def events_get(request):
# 	# REDIRECT_URI = 'https://www.getpostman.com/oauth2/callback'
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
# 		pdb.set_trace()
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
# 	# REDIRECT_URI = 'https://www.getpostman.com/oauth2/callback'
# 	# REDIRECT_URI = "https://%s%s" % (
# 	# 	get_current_site(request).domain, reverse("oauth2:return"))
# 	FLOW = flow_from_clientsecrets(
# 		CLIENT_SECRETS,
# 		scope=SCOPES,
# 		redirect_uri=REDIRECT_URI
# 	)
# 	pdb.set_trace()
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
# 			event['start']['dateTime']='2016-05-28T20:00:00-07:00'
# 		#MANDATORY ARGUMENT
# 		if 'end_datetime' in data:
# 			event['end']['dateTime']= data['end_datetime']
# 		else:
# 			event['end']['dateTime']= '2016-05-28T21:00:00-07:00'#str(datetime.datetime.now() + datetime.timedelta(hours=1))#str(timezone.now() +timezone.timedelta(hours=1))#'2016-05-28T14:00:00-07:00'

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
# 		# pdb.set_trace()
# 		# return HttpResponseRedirect("/scheduler/home")


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

# @login_required
# def index(request):
# 	pdb.set_trace()
# 	# use the first REDIRECT_URI if you are developing your app
# 	# locally, and the second in production
# 	# REDIRECT_URI = 'http://127.0.0.1:8000/scheduler/oauth2callback'
# 	# # REDIRECT_URI = "https://%s%s" % (
# 	# # 	get_current_site(request).domain, reverse("oauth2:return"))
# 	# FLOW = flow_from_clientsecrets(
# 	# 	CLIENT_SECRETS,
# 	# 	scope=SCOPES,
# 	# 	redirect_uri=REDIRECT_URI
# 	# )
# 	# user = request.user
# 	# storage = Storage(CredentialsModel, 'id', user, 'credential')
# 	# credential = storage.get()
# 	# if credential is None or credential.invalid is True:
# 	# 	FLOW.params['state'] = xsrfutil.generate_token(
# 	# 		settings.SECRET_KEY, user)
# 	# 	authorize_url = FLOW.step1_get_authorize_url()
# 	# 	f = FlowModel(id=user, flow=FLOW)
# 	# 	f.save()
# 	# 	return HttpResponseRedirect(authorize_url)
# 	# else:
# 	# 	http = httplib2.Http()
# 	# 	http = credential.authorize(http)
# 	# 	service = build('calendar', 'v3', http=http)
# 	# 	event = {
# 	# 		'summary': 'Event Check',
# 	# 		'location': '5127 Sheridan Blvd, Broomfield, CO 80020',
# 	# 		'description': 'Test for event 1',
# 	# 		'start': {
# 	# 			'dateTime': '2016-05-28T09:00:00-07:00',
# 	# 			'timeZone': 'America/Denver',
# 	# 		},
# 	# 		'end' : {
# 	# 			'dateTime': '2016-05-28T13:00:00-07:00',
# 	# 			'timeZone': 'America/Denver',
# 	# 		},
# 	# 		'recurrence': [
# 	# 			'RRULE:FREQ=DAILY;COUNT=2'
# 	# 		],
# 	# 		'reminders': {
# 	# 			'useDefault': False,
# 	# 			'overrides': [
# 	# 				{'method': 'email', 'minutes': 24 * 60},
# 	# 				{'method': 'popup', 'minutes': 10},
# 	# 			],
# 	# 		},
# 	# 	}

# 	# 	e = service.events().insert(calendarId='primary', body=event).execute()

# 	return HttpResponseRedirect("/scheduler/home")

		# return ('''*** %r event added:
		# 	Start: %s
		# 	End: $s''' (e['summary'].encode('utf-8'),
		# 		e['start']['dateTime'], e['end']['dateTime']))
		# # return render(
		# 	request, 'oauth2_authentication/main.html', {'ids':ids})


# @login_required
# @api_view(['GET','POST'])
# def event_collection(request):

# 	if request.method == 'GET':
# 		events = Event.objects.all()
# 		serializer = EventSerializer(events, many=True)
# 		return Response(serializer.data)
# 	if request.method == 'POST':
# 		event_info = request.data
# 		data = {'student':request.data.get("student_id"), 'teacher':request.data.get("teacher_id")}
# 		serializer = EventSerializer(data=data, partial=True)
# 		if serializer.is_valid():
# 			event_post(request) #sends data to create event in gCal
# 			serializer.save()
# 			return Response(serializer.data, status=status.HTTP_201_CREATED)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# 	return HttpResponse('I\'m a teapot short and stout.', status=418)

# #GET: return one event
# #POST: edit one event's skills, skills{'skill_1: True, 'skill_2':False...}
# @api_view(['GET','POST'])
# def event_element(request, pk):
# 	try:
# 		event = Event.objects.get(pk=pk)
# 	except Event.DoesNotExist:
# 		return HttpResponse(status=404)
# 	if request.method == 'GET':
# 		event = Event.objects.get(pk=pk)
# 		serializer = EventSerializer(event)
# 		return Response(serializer.data)
# 	if request.method == 'POST':
# 		data = request.data
# 		serializer = EventSerializer(event, data=data, partial=True)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data, status=status.HTTP_201_CREATED)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# 	return HttpResponse('I\'m a teapot short and stout.', status=418)

##gCal

# ###WEB Client Secrets
# ##Client_secrets = db.get..
# pdb.set_trace()
# # CLIENT_SECRETS = json.dumps({
# # 	"web":{
# # 		"client_id":"323423619559-orlpuuiaalb7sp3ooblt4mjmp32ffq1t.apps.googleusercontent.com",
# # 		"project_id":"psyched-oxide-115203",
# # 		"auth_uri":"https://accounts.google.com/o/oauth2/auth",
# # 		"token_uri":"https://accounts.google.com/o/oauth2/token",
# # 		# "client_secret":os.environ['CLIENT_SECRET'],
# # 		"client_secret": ClientSecret.objects.get(pk=1),
# # 		"redirect_uris":[
# # 			"http://127.0.0.1:8000/scheduler/complete/google-oauth2/",
# # 			"http://127.0.0.1:8000/scheduler/oauth2callback"
# # 		],
# # 		"javascript_origins":["http://localhost:8000"]
# # 	}
# # })
# # client_dict = {
# # 	"client_id" : os.environ['client_id'],
# # 	"project_id" : os.environ['project_id'],
# # 	"auth_uri" : os.environ['']
# # }

# ###LOCAL Client Secrets
# # /schedule2/scheduler/<file>
# CLIENT_SECRETS = os.path.join(
# 	os.path.dirname(__file__), 'client_secret.json')

# SCOPES = (
# 	'https://www.googleapis.com/auth/calendar',
# 	'https://www.googleapis.com/auth/drive.metadata.readonly'
# )

# REDIRECT_URI = 'http://127.0.0.1:8000/scheduler/oauth2callback'
# # REDIRECT_URI = "https://%s%s" % (
# # 	get_current_site(request).domain, reverse("scheduler:return"))

# @login_required(login_url='/scheduler/login/')
# @api_view(['GET'])
# def event_get(request, eventId):
# 	# REDIRECT_URI = 'https://www.getpostman.com/oauth2/callback'
# 	# REDIRECT_URI = "https://%s%s" % (
# 	# 	get_current_site(request).domain, reverse("scheduler:return"))
# 	pdb.set_trace()
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

# # @login_required(login_url='/scheduler/login/')
# @api_view(['GET'])
# def events_get(request):
# 	# REDIRECT_URI = 'https://www.getpostman.com/oauth2/callback'
# 	# REDIRECT_URI = "https://%s%s" % (
# 	# 	get_current_site(request).domain, reverse("scheduler:return"))
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
# 	# REDIRECT_URI = 'https://www.getpostman.com/oauth2/callback'
# 	# REDIRECT_URI = "https://%s%s" % (
# 	# 	get_current_site(request).domain, reverse("scheduler:return"))
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


# @login_required
# def auth_return(request):
# 	user = request.user
# 	if not xsrfutil.validate_token(
# 		settings.SECRET_KEY, request.GET['state'], user):
# 		return HttpResponseBadRequest()
# 	FLOW = FlowModel.objects.get(id=user).flow
# 	credential = FLOW.step2_exchange(request.GET)
# 	storage = Storage(CredentialsModel, 'id', user, 'credential')
# 	storage.put(credential)
# 	return HttpResponseRedirect("/scheduler")

	# monday_start = models.TimeField('monday start', null=True, blank=True)
	# monday_end = models.TimeField('monday end', null=True, blank=True)
	# monday_duration = models.FloatField(default=0)
	# tuesday_start = models.TimeField('tuesday start', null=True, blank=True)
	# tuesday_end = models.TimeField('tuesday end', null=True, blank=True)
	# tuesday_duration = models.FloatField(default=0)
	# wednesday_start = models.TimeField('wednesday start', null=True, blank=True)
	# wednesday_end = models.TimeField('wednesday end', null=True, blank=True)
	# wednesday_duration = models.FloatField(default=0)
	# thursday_start = models.TimeField('thursday start', null=True, blank=True)
	# thursday_end = models.TimeField('thursday end', null=True, blank=True)
	# thursday_duration = models.FloatField(default=0)
	# friday_start = models.TimeField('friday start', null=True, blank=True)
	# friday_end = models.TimeField('friday end', null=True, blank=True)
	# friday_duration = models.FloatField(default=0)
	# saturday_start = models.TimeField('saturday start', null=True, blank=True)
	# saturday_end = models.TimeField('saturday end', null=True, blank=True)
	# saturday_duration = models.FloatField(default=0)
	# sunday_start = models.TimeField('sunday start', null=True, blank=True)
	# sunday_end = models.TimeField('sunday end', null=True, blank=True)
	# sunday_duration = models.FloatField(default=0)



# #GET: show/add all open events
# @api_view(['GET'])
# def open_event(request):
# 	if request.method == 'GET':
# 		teachers = Teacher.objects.all()
# 		students = Student.objects.all()
# 		for students in student:
# 			for teacher in teacher:

	# 	teachers = Teacher.objects.all()
	# 	student_id = request.data.get('student_id')
	# 	student = Student.objects.get(student_id)
	# 	student_skills = student.get_skills()
	# 	for teacher in teachers:
	# 		teacher_skills = teacher.get_skills()
	# 		#check monday match
	# 		if student.monday_start: 
	# 			if teacher.monday_start:
	# 				if student.monday_start < teacher.monday_start:
	# 					continue;
	# 			else: 
	# 				continue;
	# 		if student.monday_end: 
	# 			if teacher.monday_end:
	# 				if student.monday_end > teacher.monday_end:
	# 					continue
	# 			else:
	# 				continue;
	# 		#check tuesday match
	# 		if student.tuesday_start: 
	# 			if teacher.tuesday_start:
	# 				if student.tuesday_start < teacher.tuesday_start:
	# 					continue
	# 			else:
	# 				continue;
	# 		if student.tuesday_end: 
	# 			if teacher.tuesday_end:
	# 				if student.tuesday_end > teacher.tuesday_end:
	# 					continue
	# 			else:
	# 				continue;
	# 		#check wednesday match
	# 		if student.wednesday_start: 
	# 			if teacher.wednesday_start:
	# 				if student.wednesday_start < teacher.wednesday_start:
	# 					continue
	# 			else:
	# 				continue;
	# 		if student.wednesday_end: 
	# 			if teacher.wednesday_end:
	# 				if student.wednesday_end > teacher.wednesday_end:
	# 					continue
	# 			else:
	# 				continue;
	# 		#check thursday match
	# 		if student.thursday_start: 
	# 			if teacher.thursday_start:
	# 				if student.thursday_start < teacher.thursday_start:
	# 					continue
	# 			else:
	# 				continue
	# 		if student.thursday_end: 
	# 			if teacher.thursday_end:
	# 				if student.thursday_end > teacher.thursday_end:
	# 					continue
	# 			else:
	# 				continue
	# 		#check friday match
	# 		if student.friday_start: 
	# 			if teacher.friday_start:
	# 				if student.friday_start < teacher.friday_start:
	# 					continue
	# 			else:
	# 				continue
						
	# 		if student.friday_end: 
	# 			if teacher.friday_end:
	# 				if student.friday_end > teacher.friday_end:
	# 					continue
	# 			else:
	# 				continue

	# 		#check saturday match
	# 		if student.saturday_start: 
	# 			if teacher.saturday_start:
	# 				if student.saturday_start < teacher.saturday_start:
	# 					continue
	# 			else:
	# 				continue
						
	# 		if student.saturday_end: 
	# 			if teacher.saturday_end:
	# 				if student.saturday_end > teacher.saturday_end:
	# 					continue
	# 			else:
	# 				continue

	# 		#check sunday match
	# 		if student.sunday_start: 
	# 			if teacher.sunday_start:
	# 				if student.sunday_start < teacher.sunday_start:
	# 					continue
	# 			else:
	# 				continue
						
	# 		if student.sunday_end: 
	# 			if teacher.sunday_end:
	# 				if student.sunday_end > teacher.sunday_end:
	# 					continue
	# 			else:
	# 				continue
	# 		#check for skills match												
	# 		for idx, skill in enumerate(student_skills):
	# 			if skill == False:
	# 				continue
	# 			if teacher_skills[idx] == False:
	# 				break

	# 		#if schedule match and skills match then create event.
	# 		data = {'student':student.student_id, 'teacher':teacher.teacher_id, 'start_datetime':student.start_datetime, 'duration':student.monday_duration, 'notes':"test note"}
	# 		#use serializer to add row to event table
	# 		serializer = EventSerializer(data=data)
	# 		if serializer.is_valid():
	# 			serializer.save()
	# 			return Response(serializer.data, status=status.HTTP_201_CREATED)
	# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	# 	return HttpResponse('I\'m a teapot short and stout.', status=418)



##old post request that creates events when only given student id.
# if request.method == 'POST':
# 		teachers = Teacher.objects.all()
# 		student_id = request.data.get('student_id')
# 		student = Student.objects.get(student_id)
# 		student_skills = student.get_skills()
# 		for teacher in teachers:
# 			teacher_skills = teacher.get_skills()
# 			###SHOULD MOVE CHECK OPERATION TO MODELS
# 			#check monday match
# 			if student.monday_start: 
# 				if teacher.monday_start:
# 					if student.monday_start < teacher.monday_start:
# 						continue;
# 				else: 
# 					continue;
# 			if student.monday_end: 
# 				if teacher.monday_end:
# 					if student.monday_end > teacher.monday_end:
# 						continue
# 				else:
# 					continue;
# 			#check tuesday match
# 			if student.tuesday_start: 
# 				if teacher.tuesday_start:
# 					if student.tuesday_start < teacher.tuesday_start:
# 						continue
# 				else:
# 					continue;
# 			if student.tuesday_end: 
# 				if teacher.tuesday_end:
# 					if student.tuesday_end > teacher.tuesday_end:
# 						continue
# 				else:
# 					continue;
# 			#check wednesday match
# 			if student.wednesday_start: 
# 				if teacher.wednesday_start:
# 					if student.wednesday_start < teacher.wednesday_start:
# 						continue
# 				else:
# 					continue;
# 			if student.wednesday_end: 
# 				if teacher.wednesday_end:
# 					if student.wednesday_end > teacher.wednesday_end:
# 						continue
# 				else:
# 					continue;
# 			#check thursday match
# 			if student.thursday_start: 
# 				if teacher.thursday_start:
# 					if student.thursday_start < teacher.thursday_start:
# 						continue
# 				else:
# 					continue
# 			if student.thursday_end: 
# 				if teacher.thursday_end:
# 					if student.thursday_end > teacher.thursday_end:
# 						continue
# 				else:
# 					continue
# 			#check friday match
# 			if student.friday_start: 
# 				if teacher.friday_start:
# 					if student.friday_start < teacher.friday_start:
# 						continue
# 				else:
# 					continue
						
# 			if student.friday_end: 
# 				if teacher.friday_end:
# 					if student.friday_end > teacher.friday_end:
# 						continue
# 				else:
# 					continue

# 			#check saturday match
# 			if student.saturday_start: 
# 				if teacher.saturday_start:
# 					if student.saturday_start < teacher.saturday_start:
# 						continue
# 				else:
# 					continue
						
# 			if student.saturday_end: 
# 				if teacher.saturday_end:
# 					if student.saturday_end > teacher.saturday_end:
# 						continue
# 				else:
# 					continue

# 			#check sunday match
# 			if student.sunday_start: 
# 				if teacher.sunday_start:
# 					if student.sunday_start < teacher.sunday_start:
# 						continue
# 				else:
# 					continue
						
# 			if student.sunday_end: 
# 				if teacher.sunday_end:
# 					if student.sunday_end > teacher.sunday_end:
# 						continue
# 				else:
# 					continue
# 			#check for skills match												
# 			for idx, skill in enumerate(student_skills):
# 				if skill == False:
# 					continue
# 				if teacher_skills[idx] == False:
# 					break

# 			#if schedule match and skills match then create event.
# 			data = {'student':student.student_id, 'teacher':teacher.teacher_id, 'start_datetime':student.start_datetime, 'duration':student.monday_duration, 'notes':"test note"}
# 			#use serializer to add row to event table
# 			serializer = EventSerializer(data=data)
# 			if serializer.is_valid():
# 				serializer.save()
# 				return Response(serializer.data, status=status.HTTP_201_CREATED)
# 			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# 		return HttpResponse('I\'m a teapot short and stout.', status=418)


###MODELS
	#Teacher's schedule: available start, availabe end, max duration(default=end-start)
	# monday_start = models.TimeField('monday start', null=True, blank=True)
	# monday_end = models.TimeField('monday end', null=True, blank=True)
	# monday_duration = models.FloatField(default=0)
	# tuesday_start = models.TimeField('tuesday start', null=True, blank=True)
	# tuesday_end = models.TimeField('tuesday end', null=True, blank=True)
	# tuesday_duration = models.FloatField(default=0)
	# wednesday_start = models.TimeField('wednesday start', null=True, blank=True)
	# wednesday_end = models.TimeField('wednesday end', null=True, blank=True)
	# wednesday_duration = models.FloatField(default=0)
	# thursday_start = models.TimeField('thursday start', null=True, blank=True)
	# thursday_end = models.TimeField('thursday end', null=True, blank=True)
	# thursday_duration = models.FloatField(default=0)
	# friday_start = models.TimeField('friday start', null=True, blank=True)
	# friday_end = models.TimeField('friday end', null=True, blank=True)
	# friday_duration = models.FloatField(default=0)
	# saturday_start = models.TimeField('saturday start', null=True, blank=True)
	# saturday_end = models.TimeField('saturday end', null=True, blank=True)
	# saturday_duration = models.FloatField(default=0)
	# sunday_start = models.TimeField('sunday start', null=True, blank=True)
	# sunday_end = models.TimeField('sunday end', null=True, blank=True)
	# sunday_duration = models.FloatField(default=0)
	###Teacher's Skills (identified through skills table)(default=False)
	# ##ACT
	# #English
	# skill_1 = models.BooleanField('ACT English', default=False)
	# #Math
	# skill_2 = models.BooleanField('ACT Math', default=False)
	# #Reading
	# skill_3 = models.BooleanField('ACT Reading', default=False)
	# #Science
	# skill_4 = models.BooleanField('ACT Science', default=False)
	# #Writing
	# skill_5 = models.BooleanField('ACT Writing', default=False)
	# ##Floor
	# #ELA
	# skill_6 = models.BooleanField('Floor ELA', default=False)
	# #Math
	# skill_7 = models.BooleanField('Floor Math', default=False)
	# ##Subject Tutoring
	# #Pre-Calc
	# skill_8 = models.BooleanField('Pre-Calculus', default=False)
	# #Calc
	# skill_9 = models.BooleanField('Calculus', default=False)
	# #Biology
	# skill_10 = models.BooleanField('Biology', default=False)
	# #Chemistry
	# skill_11 = models.BooleanField('Chemistry', default=False)
	# #Physics
	# skill_12 = models.BooleanField('Physics', default=False)
	# #Earth/Space
	# skill_13 = models.BooleanField('Earth/Space', default=False)
	# #History
	# skill_14 = models.BooleanField('History', default=False)
	# #Spanish
	# skill_15 = models.BooleanField('Spanish', default=False)

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