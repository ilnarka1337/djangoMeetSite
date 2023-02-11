from django.urls import path
from .views import *

urlpatterns = [
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
    path('<int:pk>/', ProfileDetailView.as_view(), name='profile_view'),
]
