from django.db import models
import uuid


class Question(models.Model):
    choose = tuple()
    question = models.TextField(max_length=500, verbose_name="question")
    ans1 = models.CharField(max_length=100, verbose_name="ans1")
    ans2 = models.CharField(max_length=100, verbose_name="ans2")
    ans3 = models.CharField(max_length=100, verbose_name="ans3")
    ans4 = models.CharField(max_length=100, verbose_name="ans4")

    def questions(self):
        for answering in Question.objects.all():
            self.choose = ((answering.ans1, answering.ans1),
                        (answering.ans2, answering.ans2),
                        (answering.ans3, answering.ans3),
                        (answering.ans4, answering.ans4))
        global choose
        return self.choose

    answer = models.CharField(max_length=200, choices=choose, null=True)

    def __str__(self):
        return self.question


# class QuestionForm(models.Model):
#     choose = ''
#     for answering in Question.objects.all():
#         choose = ((answering.ans1, answering.ans1),
#                   (answering.ans2, answering.ans2),
#                   (answering.ans3, answering.ans3),
#                   (answering.ans4, answering.ans4))
#     global choose
#     answer = models.CharField(max_length=200, choices=choose)
