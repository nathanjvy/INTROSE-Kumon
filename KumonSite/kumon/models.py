from django.db import models

# Create your models here.

class User(models.Model):
	username = models.CharField(max_length=25)
	password = models.CharField(max_length=50)

	def __str__(self):
		return self.username

class Student(models.Model):
    	
	gender_choices = (
		('Male','Male'),
		('Female','Female')
	)
	#Basic Details
	name = models.CharField(max_length=59)
	nickname = models.CharField(max_length=25)
	birthdate = models.DateField(auto_now=False)
	age = models.IntegerField()	
	gender = models.CharField(
		max_length=10,
		choices = gender_choices,
		default = 'Male'
	)
	picture = models.ImageField(blank=True)

	#Contact Info
	phone_num = models.CharField(max_length=15)
	tel_num = models.CharField(max_length=15)
	address = models.CharField(max_length=100)
	email = models.EmailField(max_length=50)
	student_num = models.IntegerField()

	#Other Info
	school = models.CharField(max_length=50)
	level = models.CharField(max_length=50)
	
	#Guardian Info 
	guardian_name = models.CharField(max_length=50)
	relation = models.CharField(max_length=50)
	guardian_num = models.CharField(max_length=30) #Phone / Tel
	guardian_email = models.EmailField(max_length=50,blank=True)

	def __str__(self):
		return self.name

class Teacher(models.Model):
	name = models.CharField(max_length=50)
	phone_num = models.CharField(max_length=15)
	tel_num = models.CharField(max_length=15)
	email = models.EmailField(max_length=50)
	
	def __str__(self):
		return self.name

class Schedule(models.Model):

	days_week = (
		('Monday','Monday'),
		('Tuesday','Tuesday'),
		('Wednesday','Wednesday'),
		('Thursday','Thursday'),
		('Friday','Friday'),
		('Saturday','Saturday')
	)
	
	teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
	student = models.ForeignKey(Student, on_delete=models.CASCADE)

	time_start = models.TimeField()
	time_end = models.TimeField()

	day = models.CharField(
		max_length=10,
		choices = days_week,
		default = 'Monday'
	)
	
	def __str__(self):
		return self.teacher

