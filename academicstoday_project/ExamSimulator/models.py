from django.db import models
from account.models import Student

class QuestionBank(models.Model):
    question = models.TextField()
    answer = models.TextField()
    difficulty_level = models.IntegerField()  # 1 for easy, 2 for medium, 3 for hard

class Exam(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

class UserResponse(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    question = models.ForeignKey(QuestionBank, on_delete=models.CASCADE)
    user_answer = models.TextField()
    is_correct = models.BooleanField()

class UserLevel(models.Model):
    user = models.OneToOneField(Student, on_delete=models.CASCADE)
    current_level = models.IntegerField(default=1)
