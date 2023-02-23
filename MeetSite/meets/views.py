from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from meets.models import *
from meets.forms import *
from django.shortcuts import redirect


# Create your views here.

def index(request):
    return render(request, 'meets/index.html')


class EventCreateView(CreateView):
    model = Event
    form_class = EventCreateForm
    template_name = 'meets/createEvent.html'


class EventListView(ListView):
    model = Event
    paginate_by = 20
    context_object_name = 'events'
    template_name = 'meets/events.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return Event.objects.all()


class EventDetailView(DetailView):
    model = Event
    context_object_name = 'event'
    template_name = 'meets/viewEvent.html'

    def get_context_data(self, **kwargs):
        context = super(EventDetailView, self).get_context_data()
        return context


class MeetCreateView(CreateView):
    model = Meet
    form_class = MeetCreateForm
    template_name = 'meets/createMeet.html'


class MeetsListView(ListView):
    model = Meet
    paginate_by = 20
    context_object_name = 'meets'
    template_name = 'meets/meets.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        return context

    def get_queryset(self):
        return Meet.objects.all()


class MeetDetailView(DetailView):
    model = Meet
    context_object_name = 'meet'
    template_name = 'meets/viewMeet.html'

    def get_context_data(self, **kwargs):
        context = super(MeetDetailView, self).get_context_data()
        return context
