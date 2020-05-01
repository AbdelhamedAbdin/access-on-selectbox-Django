from django.shortcuts import render
from .forms import QuestionFormView
from .models import Question


def question(request):
    class_form = QuestionFormView
    questions = Question.objects.all()
    return render(request, 'myapp/questions.html', {"forms": class_form, "questions": questions})
