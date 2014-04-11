import oauth2 as oauth
import simplejson
import time

from django.shortcuts import render_to_response
from django.conf import settings
from django.core import serializers

from models import Tweet

def import_tweets(request):
	consumer = oauth.Consumer(settings.TWITTER_CONSUMER_KEY, settings.TWITTER_CONSUMER_SECRET)
	token = oauth.Token(settings.TWITTER_ACCESS_TOKEN, settings.TWITTER_ACCESS_TOKEN_SECRET)
	client = oauth.Client(consumer, token)

	# GET YOUR PROFILE
	response, content = client.request('https://api.twitter.com/1/statuses/user_timeline.json', 'GET')

	tweets = []
	if response.status == 200:
		tweets = simplejson.loads(content)

		for tweet in tweets:
			if Tweet.objects.filter(tweet_id=long(tweet['id'])).count() < 1:
				db_tweet = Tweet()
				db_tweet.text = tweet['text']
				db_tweet.created_at = time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(tweet['created_at'],'%a %b %d %H:%M:%S +0000 %Y'))
				db_tweet.tweet_id = tweet['id']
				db_tweet.save()

	# put the logging stuff here
	return render_to_response('templates/import_tweets.html', locals())


def get_tweets(request, page=1):
	page = int(page)
	if page < 1:
		page = 1

	start = (page-1)*Tweet.ITEMS_PER_PAGE
	finish = start + Tweet.ITEMS_PER_PAGE
	serialized_tweets = serializers.serialize('json', Tweet.objects.all()[start:finish], indent=2, use_natural_keys=True)
	return render_to_response('templates/get_tweets.html', locals())