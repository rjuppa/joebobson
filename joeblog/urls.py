from django.conf.urls import patterns, url
from joeblog.views import index, contact


urlpatterns = patterns('',
    url(r'^$', index, name='index'),
    url(r'^me', contact),)
