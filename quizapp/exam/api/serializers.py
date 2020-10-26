from rest_framework import serializers
from rest_framework.authtoken.models import Token
from exam.models import Question, Student

class QuestionSerializer(serializers.ModelSerializer):
	token = serializers.SerializerMethodField()

	class Meta:
		model = Question
		fields = ['id','user','question','answer','token']


	def get_token(self,obj):
		token, created = Token.objects.get_or_create(user=obj.user)
		return token.key

class StudentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Student
		fields = '__all__'


