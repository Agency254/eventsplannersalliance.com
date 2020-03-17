from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
from epa_frontend.models import Profile, Events, EventsType, Merchants


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        related_models = User
        fields = ['user', 'email', 'bio', 'user_icon', 'country_code']
        depth = 1

    def create(self, validated_data):
        """
        Create and return a new `Profile` instance, given the validated data.
        """
        return Profile.objects.create(**validated_data)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        related_models = Profile
        fields = [
            'username', 'first_name', 'last_name'

        ]
        lookup_field = 'username'
        extra_kwargs = {
            'url': {'lookup_field': 'username'}
        }
        depth = 1


class EventsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Events
        related_models = Merchants, EventsType
        fields = [
            'id',
            'name',
            'description',
            'images',
            'merchant_id',
            'event_type_id',
            'price',
            'slug',
            'number_of_tickets',
            'tickets_sold',
            'created_at',
            'start_date',
            'end_date',
            'location',
            'published',
            'is_featured',
            'is_recommended',
        ]
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
        depth = 1

    def create(self, validated_data):
        """
        Create and return a new `Event` instance, given the validated data.
        """
        return Events.objects.create(**validated_data)


class MerchantsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Merchants
        related_models = Profile
        fields = [
            'id',
            'merchant_name',
            'merchant_description',
            'country_code',
            'created_at',
            'admin_id'
        ]
        depth = 1

    def create(self, validated_data):
        """
        Create and return a new `Merchant` instance, given the validated data.
        """
        return Merchants.objects.create(**validated_data)


class EventsTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EventsType
        related_models = Merchants
        fields = [
            'id',
            'name',
            'description',
            'merchant_id'
        ]
        depth = 1
