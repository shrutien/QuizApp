from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework import generics
from rest_framework.response import Response
from .forms import SignUpForm
from .models import Question, Choices, Student
from .api.serializers import QuestionSerializer, StudentSerializer


# from api.serializers 

# Create your views here.


class Dashboard(generics.ListAPIView):
	queryset = Question.objects.all()
	permission_classes = [permissions.IsAdminUser]
	# authentication_classes = [TokenAuthentication]
	serializer_class = QuestionSerializer




class StudentQuizPage(generics.RetrieveUpdateAPIView):
	queryset = Student.objects.all()
	permission_classes = [permissions.IsAuthenticated]
	# authentication_classes = [TokenAuthentication]
	serializer_class = StudentSerializer
	lookup_field = 'pk'





class RegisterPage(APIView):
	queryset = User.objects.all()
	permission_classes = [permissions.AllowAny]
	authentication_classes = []

	def get(self,request,*args,**kwargs):
		form = SignUpForm()
		return render(request,'exam/register.html',{'form':form})

	def post(self,request,*args,**kwargs):
		form = SignUpForm(request.POST or None)
		if form.is_valid():			
			print(form.cleaned_data)
			form.save()				
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password1')
			# user = authenticate(request, username=username, password=password)
			user_obj = User.objects.get(username=username)
			token, created = Token.objects.get_or_create(user=user_obj)
			print('Token Key: ',token.key)
			return Response({
	            'token': token.key,
	            'user_id': user_obj.pk,
	            'email': user_obj.email
        	})
			# if user is not None:
			# 	print(user)
			# 	login(request,user)
			# 	messages.success(request,'Account Created Successfully')
			# 	return redirect('dashboard')
		return render(request,'exam/register.html',{'form':form})



class LoginPage(APIView):
	queryset = User.objects.all()
	permissions_classes = [permissions.AllowAny]
	authentication_classes = []

	def get(self,request,*args,**kwargs):
		return render(request,'exam/login.html',{})

	def post(self,request,*args,**kwargs):
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request,username=username, password=password)
		user_obj = User.objects.get(username=username)
		token, created = Token.objects.get_or_create(user=user_obj)
		return Response({
            'token': token.key,
            'user_id': user_obj.pk,
            'email': user_obj.username
        })

		# if user is not None:
		# 	login(request,user)
		# 	return redirect('dashboard')
		return render(request,'exam/login.html',{})

