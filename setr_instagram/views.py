from instagram import client, subscriptions

from django.shortcuts import render_to_response
from django.conf import settings
from django.core import serializers

from models import Instagram

def import_photos(request):
	api = client.InstagramAPI(access_token='631895.91277fd.116fa05d129d435086edffc4d73b5c7b')
	photos, next = api.user_recent_media()
	
	for photo in photos:
		if Instagram.objects.filter(instagram_id=photo.id).count() < 1:
			db_photo = Instagram()
			db_photo.caption = "%s" % (photo.caption,)
			db_photo.caption = db_photo.caption.replace("Comment: maracuja said ", "")[1:-1]
			db_photo.thumbnail_image = photo.images.get('thumbnail').url
			db_photo.full_image = photo.get_standard_resolution_url()
			db_photo.link = photo.link
			db_photo.created_at = ' '.join(photo.created_time.isoformat().split('T'))
			db_photo.instagram_id = photo.id
			db_photo.save()

	# put the logging stuff here
	photos = Instagram.objects.all()
	return render_to_response('templates/import_photos.html', locals())


def get_photos(request, page=1):
	page = int(page)
	if page < 1:
		page = 1

	start = (page-1)*Instagram.ITEMS_PER_PAGE
	finish = start + Instagram.ITEMS_PER_PAGE
	serialized_photos = serializers.serialize('json', Instagram.objects.all()[start:finish], indent=2, use_natural_keys=True)
	return render_to_response('templates/get_photos.html', locals())