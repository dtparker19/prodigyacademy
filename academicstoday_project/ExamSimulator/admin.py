from django.contrib import admin
from .models import QuestionBank, Exam, UserResponse, UserLevel

admin.site.register(QuestionBank)
admin.site.register(Exam)
admin.site.register(UserResponse)
admin.site.register(UserLevel)
