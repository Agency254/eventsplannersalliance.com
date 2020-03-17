from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from epa_api import views

# Routers provide an easy way of automatically determining the URL conf.
from epa_api.views import UserViewSet, EventsListView, MerchantsListView

router = routers.DefaultRouter()
router.register(r'events', EventsListView)
router.register(r'merchants', MerchantsListView)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('api/', include(router.urls), name='api'),
]
