from django.shortcuts import render_to_response
from django.template import RequestContext


def driver(request):
    context = {}
    return render_to_response("driver.html", context, RequestContext(request))