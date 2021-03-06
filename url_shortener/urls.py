import os

from django.conf import settings
from django.conf.urls import url

from . import views

app_name = 'url_shortener'
urlpatterns = [
    url(r'^~wubenhe/$', views.index, name='index'),
    url(r'^(?P<alias>[a-zA-Z0-9]+)$', views.redirect, name='alias'),
    url(r'^(?P<alias>[a-zA-Z0-9]+)(?P<extra>/.*)$', views.redirect, name='alias'),
    url(r'^(?P<alias>[a-zA-Z0-9]+)\+$', views.preview, name='preview'),
    url(r'^(?P<alias>[a-zA-Z0-9]+)\-$', views.delete, name='delete'),
    url(r'^~analytics/$', views.analytics, name='analytics'),
    
]

# For Heroku
if 'DYNO' in os.environ:
    urlpatterns += [
        url(r'^~static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    ]
