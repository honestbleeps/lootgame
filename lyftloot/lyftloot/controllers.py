from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from lyftloot.service import LightService

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