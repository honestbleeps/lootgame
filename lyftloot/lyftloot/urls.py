"""lyftloot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import include, url, patterns
from django.contrib import admin

urlpatterns = patterns(
    '',
    (r'^public/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.BASE_DIR + '/public'}),

    url(r'^$', 'lyftloot.controllers.home', name='home'),
    url(r'^driver', 'lyftloot.controllers.driver', name='driver'),
    url(r'^passenger', 'lyftloot.controllers.passenger', name='passenger'),
    url(r'^lights/incorrect', 'lyftloot.controllers.lights_incorrect', name='lights_incorrect'),
    url(r'^lights/correct', 'lyftloot.controllers.lights_correct', name='lights_correct'),
    url(r'^admin/', include(admin.site.urls)),
)
