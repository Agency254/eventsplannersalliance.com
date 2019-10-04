from django.contrib import admin

from epa_frontend.models import Merchants, Events, Profile, Orders, OrderItems, EventsType

admin.site.register(Merchants)
admin.site.register(Events)
admin.site.register(Profile)
admin.site.register(Orders)
admin.site.register(OrderItems)
admin.site.register(EventsType)
