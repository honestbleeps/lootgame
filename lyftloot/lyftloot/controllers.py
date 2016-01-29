from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from lyftloot import service as light_service

def driver(request):
    context = {}
    return render_to_response("driver.html", context, RequestContext(request))


def passenger(request):
    context = {}
    return render_to_response("passenger.html", context, RequestContext(request))

def home(request):
    return HttpResponseRedirect("/passenger")

def lights_incorrect(request):
    light_service.incorrect()
    context = {}
    return render_to_response("test_lights.html", context, RequestContext(request))

def lights_correct(request):
    light_service.correct()
    context = {}
    return render_to_response("test_lights.html", context, RequestContext(request))