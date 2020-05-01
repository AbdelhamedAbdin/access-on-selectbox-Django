from .models import Question#, QuestionForm
from django import forms


class QuestionFormView(forms.ModelForm):
    choose = ''
    for answer in Question.objects.all():
        choose = (("A", answer.ans1),
                  ("B", answer.ans2),
                  ("C", answer.ans3),
                  ("D", answer.ans4))
    global choose
    answer = forms.CharField(widget=forms.RadioSelect(choices=choose))

    class Meta:
        model = Question
        fields = '__all__'

    def save(self, commit=True):
        form = super().save(commit=False)
        form.answer = self.cleaned_data['answer']

        if commit:
            form.save()
        return form
