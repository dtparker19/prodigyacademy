from django.db import models
from account.models import Student

class CertificationTrack(models.Model):
    name = models.CharField(max_length=100)

class BaselineQuestion(models.Model):
    track = models.ForeignKey(CertificationTrack, related_name='questions', on_delete=models.CASCADE)
    question_text = models.TextField()
    correct_answer = models.TextField()

class BaselineAssessment(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    track = models.ForeignKey(CertificationTrack, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

class UserBaselineResponse(models.Model):
    assessment = models.ForeignKey(BaselineAssessment, related_name='responses', on_delete=models.CASCADE)
    question = models.ForeignKey(BaselineQuestion, on_delete=models.CASCADE)
    user_answer = models.TextField()
