from __future__ import print_function
from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponseBadRequest
from django.core.urlresolvers import reverse
from django.views import generic
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, viewsets, permissions
from .serializers import TeacherSerializer, StudentSerializer, EventSerializer, SkillSerializer, UserSerializer, GroupSerializer
import oauth2client
from oauth2client import client, tools, file
import pdb

# #social auth
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

# #google calendar api
import os
import httplib2
from oauth2client.contrib import xsrfutil
from oauth2client.client import flow_from_clientsecrets
from oauth2client.contrib.django_orm import Storage
import apiclient
from apiclient.discovery import build
 
from django.http import HttpResponseBadRequest
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse

#models.py
from .models import Teacher, Student, Event, Skill , User,  FlowModel, CredentialsModel
from django.utils import timezone
import datetime

#other .py files
from scheduler.gCal import *
# from scheduler.login import *
from scheduler.teachers import *
from scheduler.students import *
from scheduler.events import *
from scheduler.availability import *
from scheduler.skills import *

import json

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

#python-social-auth
def login(request):
	return render(request, 'scheduler/login.html')

@login_required
def home(request):
	return render_to_response('scheduler/home.html')

def logout(request):
	auth_logout(request)
	return redirect('/scheduler/login')

@login_required
def auth_return(request):
	user = request.user
	if not xsrfutil.validate_token(
		settings.SECRET_KEY, str(request.GET['state']), user):
		return HttpResponseBadRequest()
	FLOW = FlowModel.objects.get(id=user).flow
	credential = FLOW.step2_exchange(request.GET)
	storage = Storage(CredentialsModel, 'id', user, 'credential')
	storage.put(credential)
	return HttpResponseRedirect("/scheduler/home")