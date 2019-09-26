from datetime import datetime
from django import forms
from django.contrib.auth.models import User
from django_countries.fields import CountryField

from epa_frontend.models import Properties, Orders, OrderItems, PropertyType


class PropertyTypeForm(forms.ModelForm):
    class Meta:
        model = PropertyType
        fields = ('fname', 'description', 'images')


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Properties
        fields = ('name', 'images', 'merchant_id', 'property_type_id', 'price', 'status', 'created_at', 'location')
        exclude = ('property_type_id', 'merchant_id', 'created_at', 'status')


class OrdersForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ('')
        exclude = ('')


class OrderItemsForm(forms.ModelForm):
    class Meta:
        model = OrderItems
        fields = ('')
        exclude = ('')