from django.urls import path
from . import views

urlpatterns = [
    path('', views.flashcardset_list, name='flashcardset_list'),
    path('set/<int:set_id>/', views.flashcard_list, name='flashcard_list'),
]
