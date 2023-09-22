from django.shortcuts import render
from .models import FlashcardSet, Flashcard

def flashcardset_list(request):
    flashcard_sets = FlashcardSet.objects.all()
    return render(request, 'flashcards/flashcardset_list.html', {'flashcard_sets': flashcard_sets})

def flashcard_list(request, set_id):
    flashcards = Flashcard.objects.filter(flashcard_set_id=set_id)
    return render(request, 'flashcards/flashcard_list.html', {'flashcards': flashcards})


