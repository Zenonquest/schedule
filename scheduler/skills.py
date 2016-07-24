from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, viewsets, permissions

from django.contrib.auth.decorators import login_required

from .models import Skill
from .serializers import SkillSerializer

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

#Parameters: Skill pk
#Body: {"skill_1":"True", "teacher":1}
#GET: return all skills lists
#POST: edit one skill list, request must be dictionary w ALL skills (skills{'skill_1: True, 'skill_2':False..., 'skill_15:True'})
@api_view(['GET', 'POST'])
def skill_element(request, pk):
	try:
		skill = Skill.objects.get(pk=pk)
	except Skill.DoesNotExist:
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

@api_view(['GET', 'POST'])
def skill_byteacher(request, teacher_id):
	try:
		skill = Skill.objects.get(teacher_id = teacher_id)
	except Skill.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'POST':
		data = request.data
		serializer =SkillSerializer(skill, data=data, partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	return HttpResponse('I\'m a teapot short and stout.', status=418)