from django.db import models
from django.contrib import admin


class Instagram(models.Model):
    caption = models.CharField(max_length=255)
    thumbnail_image = models.CharField(max_length=255)
    full_image = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    instagram_id = models.CharField(max_length=50)

    ITEMS_PER_PAGE = 10

    def __unicode__(self):
        return "%s - %s" % (self.created_at, self.caption)

    class Meta:
        ordering = ["-created_at"]


class InstagramAdmin(admin.ModelAdmin):
    list_display = ('caption', 'link',)


admin.site.register(Instagram, InstagramAdmin)