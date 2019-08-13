from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from .serializers import EfemerideViewSet

class _DefaultRouter(DefaultRouter):
    def __init__(self):
        self.trailing_slash = '/?'
        super(DefaultRouter, self).__init__()


router = _DefaultRouter()
router.register(r'efemerides', EfemerideViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]