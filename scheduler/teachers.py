from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, viewsets, permissions

from .models import Teacher

from .serializers import TeacherSerializer


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
@api_view(['GET', 'POST', 'DELETE'])
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


	if request.method == 'DELETE':
		teacher.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)