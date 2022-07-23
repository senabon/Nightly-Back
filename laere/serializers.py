from dataclasses import fields
from multiprocessing import Event
import laere 
from rest_framework import serializers
from .models import User, Event #, Ratings

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event 
        fields = ('id', 'state', 'city', 'url', 'location', 'host', 'description', 'dateTime', 'photo_url', 'city_state')


#class RatingsSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Ratings 
#        fields = ('rating','comment')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model: User
        fields =  ('first_name', 'last_name', 'state', 'city')

