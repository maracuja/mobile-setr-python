from django.db import models
from django.contrib import admin


class Tweet(models.Model):
	text = models.CharField(max_length=140)
	created_at = models.DateTimeField()
	tweet_id = models.BigIntegerField()
	visible = models.BooleanField(default=True)

	ITEMS_PER_PAGE = 10
	
	def __unicode__(self):
		return "%s - %s" % (self.created_at, self.text)

	class Meta:
		ordering = ["-created_at"]


class TweetAdmin(admin.ModelAdmin):
    list_display = ('text', 'created_at', 'visible',)


admin.site.register(Tweet, TweetAdmin)