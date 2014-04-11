from django.db import models
from django.contrib import admin


class SetrProject(models.Model):
    name = models.CharField(max_length=200)
    client = models.CharField(max_length=200)
    description = models.TextField()
    link = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    visible = models.BooleanField(default=True)

    class Meta:
        ordering = ["-created_at"]


class SetrProjectImage(models.Model):
    project = models.ForeignKey(SetrProject)
    image = models.ImageField(upload_to='uploads/')


class SetrProjectImageInline(admin.StackedInline):
    model = SetrProjectImage
    extra = 2


class SetrProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'link',)
    inlines = [SetrProjectImageInline]


admin.site.register(SetrProject, SetrProjectAdmin)