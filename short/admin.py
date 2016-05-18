from django.contrib import admin

# Register your models here.
from .models import Shorts

class ShortsModelAdmin(admin.ModelAdmin):
	list_display = ["incomingurl","outgoingurl1","updated","timestamp"]
	list_display_links= ["updated"]
	list_editable =["incomingurl","outgoingurl1",]
	list_filter =["incomingurl","outgoingurl1","updated","timestamp"]

	search_field = ["incomingurl","outgoingurl1","updated","timestamp"]
	class Meta:
		model =Shorts


admin.site.register(Shorts, ShortsModelAdmin)
