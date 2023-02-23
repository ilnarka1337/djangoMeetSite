from django.urls import path
from .views import *
from django.contrib import admin

urlpatterns = [
    path('', index, name='home'),
    path('meets/', MeetsListView.as_view(), name='meets'),
    path('events/', EventListView.as_view(), name='events'),
    path('add-event/', EventCreateView.as_view(), name='addEvent'),
    path('add-meet/', MeetCreateView.as_view(), name='addMeet'),
    path('event/<int:pk>/', EventDetailView.as_view(), name='viewEvent'),
    path('meet/<int:pk>/', MeetDetailView.as_view(), name='viewMeet'),
]