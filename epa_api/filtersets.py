from django_filters import rest_framework as filters

from epa_frontend.models import Events


class EventsFilter(filters.FilterSet):
    class Meta:
        model = Events
        fields = ['published', 'is_free', 'is_featured', 'is_recommended']
