from django import forms

from .models import User, Student, Teacher
	
class LoginForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ['username', 'password']
		widgets = {
			'password': forms.PasswordInput(),
		}

class StudentForm(forms.ModelForm):

	class Meta:
		model = Student
		fields = ['name','nickname','birthdate','age',
                          'gender','picture','phone_num','tel_num',
                          'address','email','student_num','school',
                          'school_level','kumon_level','guardian_name',
                          'relation','guardian_name','guardian_email'
                ]


class TeacherForm(forms.ModelForm):

        class Meta:
                model = Teacher
                fields = ['name','phone_num','tel_num','email']
		
