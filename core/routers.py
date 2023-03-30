from rest_framework import routers
from core.auth.viewsets.login import LoginViewSet
from core.auth.viewsets.refresh import RefreshViewSet
from core.auth.viewsets.register import RegisterViewSet
from core.user.viewsets import UserViewSet
from core.event.viewsets import EventViewSet

router = routers.SimpleRouter()


# event app
router.register(r'event', EventViewSet, basename='event')



# auth app
router.register(r'auth/register', RegisterViewSet, basename='auth-register')
router.register(r'auth/login', LoginViewSet, basename='auth-login')
router.register(r'auth/refresh', RefreshViewSet,basename='auth-refresh')

# User APP
router.register(r'user', UserViewSet, basename='user')
urlpatterns = [
    *router.urls,
]