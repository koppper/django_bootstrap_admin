from django.contrib import admin
from .models import User, Speakers


class SpeakersAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_filter = ("id", "name")


admin.site.register(User)
admin.site.register(Speakers, SpeakersAdmin)
