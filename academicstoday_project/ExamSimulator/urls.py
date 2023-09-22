from django.urls import path
from . import views

urlpatterns = [
    path('start/', views.start_exam, name='start_exam'),
    path('end/<int:exam_id>/', views.end_exam, name='end_exam'),
    path('summary/<int:exam_id>/', views.exam_summary, name='exam_summary'),
]
