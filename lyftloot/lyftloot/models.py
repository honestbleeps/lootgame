from django.contrib.auth.models import User
from django.db import models


class QuizQuestion(models.Model):
    question = models.TextField()

    class Meta:
        db_table = "questions"


class QuizAnswer(models.Model):
    question = models.ForeignKey(QuizQuestion)
    answer = models.TextField()
    correct = models.BooleanField()

    class Meta:
        db_table = "answers"


class Quiz(models.Model):
    user = models.ForeignKey(User)
    started_at = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        db_table = "quizzes"


class UserAnswer(models.Model):
    quiz = models.ForeignKey(Quiz)
    question = models.ForeignKey(QuizQuestion)
    answer = models.ForeignKey(QuizAnswer)

    class Meta:
        db_table = "user_answers"
        unique_together = ("quiz", "question")
