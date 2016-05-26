from django.contrib.auth.decorators import login_required
import oauth2client
from oauth2client import client, tools, file
from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout


def login(request):
	# context = RequestContext(request, {
	#     'request': request, 'user': request.user})
	# return render_to_response('login.html', context_instance=context)
	return render(request, 'scheduler/login.html')


@login_required(login_url='/')
def home(request):
	return render_to_response('scheduler/home.html')


def logout(request):
	auth_logout(request)
	return redirect('/scheduler/login')
