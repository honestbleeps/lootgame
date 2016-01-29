from django.contrib import admin
from models import QuizQuestion, QuizAnswer, Quiz, UserAnswer


class QuizQuestionAdmin(admin.ModelAdmin):
    list_display = ["id", "question",]
    search_fields = ["question"]

admin.site.register(QuizQuestion, QuizQuestionAdmin)


class QuizAnswerAdmin(admin.ModelAdmin):
    list_display = ["id", "question", "answer", "correct"]

admin.site.register(QuizAnswer, QuizAnswerAdmin)


class QuizAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "started_at", "correct_answers", "incorrect_answers", "total_answers"]
    readonly_fields = ["correct_answers", "incorrect_answers", "total_answers", "started_at"]

    def correct_answers(self, obj):
        return "<span style='color: green'>{}</span>".format(
            UserAnswer.objects.filter(quiz=obj, answer__correct=True).count())
    correct_answers.short_description = "Corrects"
    correct_answers.allow_tags = True

    def incorrect_answers(self, obj):
        return "<span style='color: red'>{}</span>".format(
            UserAnswer.objects.filter(quiz=obj, answer__correct=False).count())
    incorrect_answers.short_description = "Incorrects"
    incorrect_answers.allow_tags = True

    def total_answers(self, obj):
        return UserAnswer.objects.filter(quiz=obj).count()
    total_answers.short_description = "Total"

admin.site.register(Quiz, QuizAdmin)


class UserAnswerAdmin(admin.ModelAdmin):
    list_display = ["id", "quiz", "is_correct"]
    readonly_fields = ["is_correct"]

    def is_correct(self, obj):
        return obj.answer.correct
    is_correct.short_description = "Correct?"
    is_correct.boolean = True

admin.site.register(UserAnswer, UserAnswerAdmin)