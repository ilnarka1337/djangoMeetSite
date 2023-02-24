from django.contrib import admin
from meets.models import *


class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "photo")


# Register your models here.
admin.site.register(Meet)
admin.site.register(Event, EventAdmin)
