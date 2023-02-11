from rest_framework import serializers
from users.models import MeetsUser
from meets.models import Event, Meet


class UserSerializer(serializers.ModelSerializer):
    created_meets = serializers.RelatedField(many=True, read_only=True)
    created_events = serializers.RelatedField(many=True, read_only=True)

    class Meta:
        model = MeetsUser
        fields = ['id', 'username', 'date_joined', 'created_meets', 'created_events']


class EventSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    views = serializers.ReadOnlyField()

    class Meta:
        model = Event
        fields = ['id', 'title', 'e_date', 'e_time', 'owner', 'views', 'status']
