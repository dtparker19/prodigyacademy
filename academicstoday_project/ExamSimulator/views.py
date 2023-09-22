from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import QuestionBank, Exam, UserResponse, UserLevel

@login_required
def start_exam(request):
    user = request.user
    user_level, created = UserLevel.objects.get_or_create(user=user)

    questions = QuestionBank.objects.filter(difficulty_level=user_level.current_level)[:10]  # Fetch 10 questions for example
    exam = Exam.objects.create(user=user)

    return render(request, 'start_exam.html', {'questions': questions, 'exam_id': exam.id})

@login_required
def end_exam(request, exam_id):
    exam = Exam.objects.get(id=exam_id)
    user_responses = UserResponse.objects.filter(exam=exam)

    correct_answers = 0
    for response in user_responses:
        if response.is_correct:
            correct_answers += 1

    user_level = UserLevel.objects.get(user=exam.user)
    if correct_answers > 7:  # Thresholds are just examples
        user_level.current_level += 1
    elif correct_answers < 4:
        user_level.current_level = max(1, user_level.current_level - 1)

    user_level.save()

    return redirect('ExamSimulator/exam_summary', exam_id=exam.id)

@login_required
def exam_summary(request, exam_id):
    exam = Exam.objects.get(id=exam_id)
    user_responses = UserResponse.objects.filter(exam=exam)

    return render(request, 'ExamSimulator/exam_summary.html', {'user_responses': user_responses})
