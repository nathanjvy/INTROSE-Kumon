from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

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
	school_level = models.CharField(max_length=50)
	kumon_level = models.CharField(max_length=50)

	#Guardian Info 
	guardian_name = models.CharField(max_length=50)
	relation = models.CharField(max_length=50)
	guardian_num = models.CharField(max_length=30) #Phone / Tel
	guardian_email = models.EmailField(max_length=50,blank=True)

        #teacher/s will be found in schedule
	schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)

	#Payment Status
	tuition_fee = models.CharField(max_length=50)
	status_choices = (
                ('Paid','paid'),
                ('Unpaid','unpaid')
        )
	
	tuition_status = models.CharField(
                max_length=10,
                choices = status_choices,
                default = 'Unpaid'
        )
                
	def __str__(self):
		return self.name

class Teacher(models.Model):
	name = models.CharField(max_length=50)
	phone_num = models.CharField(max_length=15)
	tel_num = models.CharField(max_length=15)
	email = models.EmailField(max_length=50)
	t_picture = models.ImageField(blank=True)
	
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
	#student = models.ForeignKey(Student, on_delete=models.CASCADE)

	time_start = models.TimeField()
	time_end = models.TimeField()

	day = models.CharField(
		max_length=10,
		choices = days_week,
		default = 'Monday'
	)
	
	def __str__(self):
		return self.teacher
class Grades(models.Model):

        subject_choice = (
                ('Science', 'Sci'),
                ('Math', 'Math'),
                ('English', 'Eng')
        )
        subject = models.CharField(choices=subject_choice, max_length=10)

        #grade for this term/sem/whatever they call it sa kumon
        curr_grade = models.IntegerField(
                default=0,
                validators=[
                        MaxValueValidator(100),
                        MinValueValidator(0)
                ]
        )

        #average grade, cgpa for the subj kumaga
        #ave_grade = 0
        #ave_grade = models.IntegerField((curr_grade + ave_grade) / 2)

