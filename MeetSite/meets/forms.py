import re
from django.forms import ModelForm, ImageField, FileField, FileInput
from .models import *


class EventCreateForm(ModelForm):
    class Meta:
        model = Event
        fields = "__all__"


class MeetCreateForm(ModelForm):
    class Meta:
        model = Meet
        fields = ('title', 'meet_event', 'm_date', 'm_time', 'location', 'info', 'm_photo', 'status')
