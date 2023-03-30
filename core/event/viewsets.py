from http.client import responses
from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.core.exceptions import ObjectDoesNotExist
from core.event.serializers import EventSerializer
from core.event.models import Event
from core.user.models import User


        
def isAuth(currentUser):
        try:
            user_details=User.objects.get(username=currentUser)
            return user_details.id
        except Event.DoesNotExist:
            raise Http404

class EventViewSet(viewsets.ModelViewSet):
    http_method_names = ('get','post','delete','post')
    permission_classes = (IsAuthenticated,)
    serializer_class = EventSerializer

    def get_queryset(self):
        try:
            if self.request.user.is_authenticated:
                currentUser=self.request.user.username
                return Event.objects.filter(user_id=isAuth(currentUser))
        except Event.DoesNotExist:
            raise Http404
        

    def get_object_by_id(self, public_id):
        try:
            instance = self.get(public_id=public_id)
            return instance
        except (ObjectDoesNotExist, ValueError, TypeError):
            return Http404


    def delete(self, public_id):
        try:
            instance = self.get(public_id=public_id)
            instance.delete()
            return responses(instance)

        except (ObjectDoesNotExist, ValueError, TypeError):
            return Http404


