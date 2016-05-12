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
