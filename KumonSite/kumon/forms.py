from django import forms

from .models import User,Student
	
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
		fields = ['birthdate']
		