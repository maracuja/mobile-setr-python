from django.conf.urls.defaults import *

urlpatterns = patterns('',
	(r'^get/(?P<page>[\d]+)/?', 'setr_instagram.views.get_photos'),
    (r'^get', 'setr_instagram.views.get_photos'),
	(r'^import', 'setr_instagram.views.import_photos'),
)
