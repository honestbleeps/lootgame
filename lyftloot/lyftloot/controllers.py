from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.views.decorators.http import require_POST
from models import QuizAnswer, Quiz, QuizQuestion, UserAnswer, User

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
    ls.correct()
    context = {
        'lights': 'correct'
    }
    return render_to_response("test_lights.html", context, RequestContext(request))


def lights_game_end(request):
    ls = LightService()
    ls.game_end()
    context = {
        'lights': 'game_end'
    }
    return render_to_response("test_lights.html", context, RequestContext(request))


@require_POST
def quiz_passenger(request):
    """ Serve up the next question with all possible answers
    """
    print "request.POST: ", request.POST
    context = {}
    ls = LightService()

    # This is an either an answer to a question or a prompt to move to the next question
    # Either way, retrieve the current quiz id, passed in via POST
    quiz_id = request.POST.get("quiz_id")
    quiz = get_object_or_404(Quiz, pk=quiz_id)

    # Also attempt to retrieve an answer_id. If it doesn't exist, this is just a prompt
    # to move to the next question
    answer_id = request.POST.get("answer")

    if answer_id:
        user_answer, created = UserAnswer.objects.get_or_create(quiz_id=quiz_id, answer_id=answer_id)
        is_correct = user_answer.answer.correct
        context["previous_question"] = user_answer.answer.question
        context["previous_answer"] = user_answer.answer
        context["previous_answer_was_correct"] = is_correct
        context["previous_possible_answers"] = QuizAnswer.objects.filter(question_id=user_answer.answer.question.id)

        if is_correct:
            ls.correct()
        else:
            ls.incorrect()

    # Retrieve a question the user hasn't answered yet
    already_answered = UserAnswer.objects.filter(quiz_id=quiz.id)
    print "already_answered: ", already_answered
    already_answered_ids = [a.answer.question.id for a in already_answered]
    question = QuizQuestion.objects.exclude(id__in=already_answered_ids).first()

    if question:
        possible_answers = QuizAnswer.objects.filter(question_id=question.id)

        context["next_question"] = question
        context["next_possible_answers"] = possible_answers

    context["quiz_id"] = quiz_id

    return render_to_response("quiz_passenger.html", context, RequestContext(request))


def quiz_passenger_intro(request):
    # Create a new Quiz object
    # HACKTACULAR! hard code user to 1! This makes me a sad panda.
    the_user = User.objects.get(id=1)
    quiz = Quiz.objects.create(user=the_user)

    return render_to_response("quiz_passenger_intro.html", {"quiz_id": quiz.id}, RequestContext(request))


def quiz_end_sequence(request, quiz_id):
    all_answers = UserAnswer.objects.filter(quiz_id=quiz_id)
    answers_correct = UserAnswer.objects.filter(quiz_id=quiz_id, answer__correct=True).count()
    lyft_credit = answers_correct * 5
    context = {
        "lyft_credit": lyft_credit,
        "quiz_id": quiz_id,
        "all_answers": all_answers,
        "all_answers_count": all_answers.count(),
        "correct_answers_count": answers_correct,
    }

    return render_to_response("quiz_end_sequence.html", context, RequestContext(request))
