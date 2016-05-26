from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, viewsets, permissions

from django.contrib.auth.decorators import login_required

from .models import Availability
from .serializers import AvailabilitySerializer

#GET: return all skills lists
#POST: add one skill list, request must be dictionary w ALL availability (availability{'skill_1: True, 'skill_2':False..., 'skill_15:True'})
@api_view(['GET', 'POST'])
def availability_collection(request):
	if request.method == 'GET':
		availability = Availability.objects.all()
		serializer = AvailabilitySerializer(availability, many=True)
		return Response(serializer.data)
	if request.method == 'POST':
		data = request.data
		serializer = AvailabilitySerializer(data=data, partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	return HttpResponse('I\'m a teapot short and stout.', status=418)


#GET: return all availability lists
#POST: edit one skill list, request must be dictionary w ALL availability (availability{'skill_1: True, 'skill_2':False..., 'skill_15:True'})
@api_view(['GET', 'POST'])
def availability_element(request, pk):
	try:
		availability = Availability.objects.get(pk=pk)
	except Teacher.DoesNotExist:
		return HttpResponse(status=404)
		
	if request.method == 'GET':
		serializer = AvailabilitySerializer(availability)
		return Response(serializer.data)

	if request.method == 'POST':
		data = request.data
		serializer =AvailabilitySerializer(availability, data=data, partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	return HttpResponse('I\'m a teapot short and stout.', status=418)