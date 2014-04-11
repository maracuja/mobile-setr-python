from django.conf.urls.defaults import *

urlpatterns = patterns('',
	(r'^get/(?P<page>[\d]+)/?', 'setr_twitter.views.get_tweets'),
    (r'^get', 'setr_twitter.views.get_tweets'),
	(r'^import', 'setr_twitter.views.import_tweets'),
)
