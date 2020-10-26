from django.urls import path
from django.conf.urls import url
from .views import Dashboard,RegisterPage,LoginPage,StudentQuizPage

urlpatterns=[
	url(r'^$', RegisterPage.as_view(), name='register'),	
	url(r'^dashboard/', Dashboard.as_view(), name='dashboard'),
	url(r'^login_page/', LoginPage.as_view(), name='login_page'),
	path('student_exam/<int:pk>/', StudentQuizPage.as_view(), name='student_exam'),
]