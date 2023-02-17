from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import *
from .permissions import IsOwnerOrReadOnly
from users.models import MeetsUser
from meets.models import Event, Meet


class UserList(generics.ListAPIView):
    queryset = MeetsUser.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = MeetsUser.objects.all()
    serializer_class = UserSerializer


class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


class MeetList(generics.ListCreateAPIView):
    queryset = Meet.objects.all()
    serializer_class = MeetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class MeetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Meet.objects.all()
    serializer_class = MeetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
# Представлению PostList требуется разрешение IsAuthenticatedOrReadOnly, потому что пользователь
# должен аутентифицироваться, чтобы создать пост, а вот просматривать список может любой пользователь.

# Для PostDetails нужны оба разрешения, поскольку обновлять или удалять пост должен только залогиненный пользователь,
# а также его владелец. Для получения поста прав не нужно. Вернитесь на http://127.0.0.1:8000/posts.
# Зайдите в учетную запись admin и другие, чтобы проверить, какие действия доступны аутентифицированным и
# анонимным пользователям.

# Будучи разлогиненным, вы не должны иметь возможность создавать, удалять или обновлять посты.
# При аутентификации вы не должны иметь право удалять или редактировать чужие посты.
