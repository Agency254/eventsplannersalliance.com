from django.contrib import admin

from epa_frontend.models import Merchants, Properties, Profile, Orders, OrderItems, PropertyType

admin.site.register(Merchants)
admin.site.register(Properties)
admin.site.register(Profile)
admin.site.register(Orders)
admin.site.register(OrderItems)
admin.site.register(PropertyType)
