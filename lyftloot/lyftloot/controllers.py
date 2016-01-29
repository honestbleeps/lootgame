from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from models import QuizAnswer, Quiz, QuizQuestion, UserAnswer

from service import LightService


def driver(request):
    context = {}
    return render_to_response("driver.html", context, RequestContext(request))


def passenger(request):
    context = {}
    return render_to_response("passenger.html", context, RequestContext(request))


def home(request):
    return HttpResponseRedirect("/passenger")


def lights_game_start(request):
    ls = LightService()
    ls.game_start()
    context = {
        'lights': 'game_start'
    }
    return render_to_response("test_lights.html", context, RequestContext(request))


def lights_incorrect(request):
    ls = LightService()
    ls.incorrect()
    context = {
        'lights': 'incorrect'
    }
    return render_to_response("test_lights.html", context, RequestContext(request))


def lights_correct(request):
    ls = LightService()
    print ls
    ls.correct()
    context = {
        'lights': 'correct'
    }
    return render_to_response("test_lights.html", context, RequestContext(request))


def quiz_passenger(request):
    print "request.method: ", request.method
    print "request.POST: ", request.POST
    print "request.GET: ", request.GET
    ls = LightService()
    correct = None
    is_game_start = False
    if request.method == "GET":
        # This is the first visit, create a new quiz!
        quiz = Quiz.objects.create(user=request.user)
        is_game_start = True
        # ls.game_start()
        quiz_id = quiz.id
    else:
        # This is an answer to a question, so retrieve the current quiz id,
        # passed in via POST
        quiz_id = request.POST.get("quiz_id")
        answer_id = request.POST.get("answer")

        user_answer, created = UserAnswer.objects.get_or_create(quiz_id=quiz_id, answer_id=answer_id)
        correct = user_answer.answer.correct
        if correct:
            ls.correct()
        else:
            ls.incorrect()

    get_object_or_404(Quiz, pk=quiz_id)

    # Retrieve a question the user hasn't answered yet
    already_answered = UserAnswer.objects.filter(quiz_id=quiz_id)
    already_answered = [a.answer.question.id for a in already_answered]
    question = QuizQuestion.objects.exclude(id__in=already_answered).first()

    if question:
        possible_answers = QuizAnswer.objects.filter(question_id=question.id)

        context = {
            "question": question,  # Note this could be None
            "possible_answers": possible_answers,
        }
    else:
        all_answers = UserAnswer.objects.filter(quiz_id=quiz_id)
        context = {
            "quiz_finished": True,
            "all_answers": all_answers,
            "all_answers_count": all_answers.count(),
            "correct_answers_count": UserAnswer.objects.filter(quiz_id=quiz_id, answer__correct=True).count(),
        }

    if correct is not None:
        context["correct"] = correct
    if is_game_start:
        context["game_start"] = True
    context["quiz_id"] = quiz_id

    return render_to_response("quiz_passenger.html", context, RequestContext(request))

