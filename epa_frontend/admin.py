from django.contrib import admin

from epa_frontend.models import Merchants, Events, Profile, EventsType

admin.site.register(Merchants)
admin.site.register(Events)
admin.site.register(Profile)
admin.site.register(EventsType)
