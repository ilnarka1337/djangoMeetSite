from django.urls import path, include
import rest_framework
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = [
    path('auth/', include('rest_framework.urls')),
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
    path('events/', EventList.as_view()),
    path('events/<int:pk>/', EventDetail.as_view()),
    path('meets/', MeetList.as_view()),
    path('meets/<int:pk>', MeetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
