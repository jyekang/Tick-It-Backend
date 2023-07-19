from rest_framework import serializers
from .models import Venue, Event

class VenueSerializer(serializers.HyperlinkedModelSerializer):
    events = serializers.HyperlinkedRelatedField(
        view_name='event_detail',
        many=True,
        read_only=True
    )
    class Meta:
       model = Venue
       fields = ('id', 'name', 'location', 'capacity', 'website_url', 'events')


class EventSerializer(serializers.HyperlinkedModelSerializer):
    venue = serializers.HyperlinkedRelatedField(
        view_name='venue_detail',
        read_only=True
    )
    class Meta:
       model = Event
       fields = ('id', 'name', 'date', 'time', 'ticket_price', 'city', 'state', 'venue')