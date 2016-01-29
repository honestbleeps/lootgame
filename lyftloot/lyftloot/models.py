from django.contrib.auth.models import User
from django.db import models


class QuizQuestion(models.Model):
    question = models.TextField()

    class Meta:
        db_table = "questions"

    def __unicode__(self):
        return self.question[0:min(400, len(self.question))]


class QuizAnswer(models.Model):
    question = models.ForeignKey(QuizQuestion)
    answer = models.TextField()
    correct = models.BooleanField()

    class Meta:
        db_table = "answers"

    def __unicode__(self):
        return u"{}: {}: {}".format(self.question,
                                    self.answer[0:min(400, len(self.answer))],
                                    self.correct)


class Quiz(models.Model):
    user = models.ForeignKey(User)
    started_at = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        db_table = "quizzes"

    def __unicode__(self):
        return u"{} {} {}".format(self.user.username, self.id, self.started_at)


class UserAnswer(models.Model):
    quiz = models.ForeignKey(Quiz)
    answer = models.ForeignKey(QuizAnswer)

    class Meta:
        db_table = "user_answers"

    def __unicode__(self):
        return u"{}: {}".format(self.quiz.user.username, self.answer)
