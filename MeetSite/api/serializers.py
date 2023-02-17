from rest_framework import serializers
from users.models import MeetsUser
from meets.models import Event, Meet


class UserSerializer(serializers.ModelSerializer):
    created_meets = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title')
    created_events = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title')

    class Meta:
        model = MeetsUser
        fields = ['id', 'username', 'date_joined', 'created_meets', 'created_events']


class EventSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    views = serializers.ReadOnlyField()

    class Meta:
        model = Event
        fields = ['id', 'title', 'e_date', 'e_time', 'owner', 'views', 'status']


class MeetSerializer(serializers.ModelSerializer):
    meet_event = serializers.SlugRelatedField(read_only=True, slug_field='title')
    status = serializers.ChoiceField(choices=Meet.STATUS_OF_MEET, source='get_status_display')
    people = serializers.IntegerField(read_only=True, source='meet_users.count')

    class Meta:
        model = Meet
        fields = ['id', 'title', 'm_date', 'm_time', 'meet_event', 'owner', 'status', 'people']
