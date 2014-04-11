from django.shortcuts import render_to_response

from setr_instagram.models import Instagram
from setr_twitter.models import Tweet
from setr_projects.models import SetrProject

from django.conf import settings

def home(request):
	tweets = Tweet.objects.all()[:20]
	instagrams = Instagram.objects.all()[:20]

	projectimages = []
	projects = SetrProject.objects.all()
	for project in projects:
		for image in project.setrprojectimage_set.all():
			projectimages.append(image.image)

	media_url = settings.MEDIA_URL
	static_url = settings.STATIC_URL
	return render_to_response('templates/home.html', locals())