
from django.db.models import fields
from rest_framework import serializers
from .models import Event
 
class EventSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)
    class Meta:
        model = Event
        fields = ('id','user','title', 'body', 'created','updated')


       