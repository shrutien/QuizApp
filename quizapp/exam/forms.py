#UserCreationForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
	email = forms.EmailField(max_length=255)
	first_name = forms.CharField(max_length=255)

	class Meta:
		model = User
		fields = ['username','password1','password2','email','first_name']


	def clean_username(self):
		username = self.cleaned_data.get('username')
		username_value = User.objects.filter(username=username)
		if username_value.count():
			raise forms.ValidationError('Email Already Exists')
		return username


	def clean_email(self):
		email = self.cleaned_data.get('email')
		email_value = User.objects.filter(email=email)
		if email_value.count():
			raise forms.ValidationError('Email Already Exists')
		return email

	def clean_password2(self):
		password = self.cleaned_data.get('password1')
		confirm_password = self.cleaned_data.get('password2')

		if password != confirm_password:
			raise forms.ValidationError('Password and ConfirmPassword does not match.')
		return confirm_password
	
	def save(self, commit=True):
		print(self.cleaned_data.get('username'))
		print(self.cleaned_data.get('email'))
		user = User.objects.create_user(self.cleaned_data.get('username'),self.cleaned_data.get('email'))
		user.set_password(self.cleaned_data.get('password'))
		user.save()
		return user
