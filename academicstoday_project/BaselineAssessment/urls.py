from django.urls import path
from . import views

urlpatterns = [
    path('start/<int:track_id>/', views.start_assessment, name='start_assessment'),
    path('submit/<int:assessment_id>/', views.submit_assessment, name='submit_assessment'),
]
