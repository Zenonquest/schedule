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