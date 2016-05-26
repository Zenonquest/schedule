from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, viewsets, permissions

from .models import Student
from .serializers import StudentSerializer
#GET: return all students
#POST: create student (body needs student_name)
@api_view(['GET', 'POST'])
def student_collection(request):
	if request.method == 'GET':
		students = Student.objects.all()
		serializer = StudentSerializer(students, many=True)
		return Response(serializer.data)
	
	if request.method == 'POST':
		data = request.data
		serializer = StudentSerializer(data=data, partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	return HttpResponse('I\'m a teapot short and stout.', status=418)

#return all students
#edit student. all fields available
@api_view(['GET', 'POST'])
def student_element(request, pk):
	try:
		student = Student.objects.get(pk=pk)
	except Student.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializer = StudentSerializer(student)
		return Response(serializer.data)

	if request.method == 'POST':
		data = request.data
		serializer = StudentSerializer(student, data=data, partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	return HttpResponse('I\'m a teapot short and stout.', status=418)