from django.db import models
from django.contrib import admin


class NikePlusRun(models.Model):
	run_id = models.CharField(max_length=20)
	start_time = models.DateTimeField()
	distance = models.DecimalField(max_digits=6, decimal_places=4)
	duration = models.IntegerField()
	calories = models.DecimalField(max_digits=5, decimal_places=1)
	description = models.TextField(max_length=200)
	how_felt = models.IntegerField()
	weather = models.IntegerField()
	terrain = models.IntegerField()
	gpxid = models.CharField(max_length=100)
	equipment_type = models.CharField(max_length=50)
	visible = models.BooleanField(default=True)


class NikePlusRunAdmin(admin.ModelAdmin):
    list_display = ('start_time', 'distance',)


admin.site.register(NikePlusRun, NikePlusRunAdmin)