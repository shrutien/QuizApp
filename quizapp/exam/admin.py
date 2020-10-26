from django.contrib import admin
from .models import Question, Choices,Student

# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
	list_display = ['user','question']

	class Meta:
		model = Question
		fields = '__all__'


admin.site.register(Question,QuestionAdmin)

class ChoicesAdmin(admin.ModelAdmin):
	list_display = ['question','choice_a']
	class Meta:
		model = Choices
		fields = '__all__'

admin.site.register(Choices,ChoicesAdmin)


class StudentAdmin(admin.ModelAdmin):
	list_display = ['user','question']
	class Meta:
		model = Student
		fields = '__all__'

admin.site.register(Student,StudentAdmin)