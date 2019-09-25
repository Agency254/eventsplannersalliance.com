from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField
from djmoney.models.fields import MoneyField
from datetime import datetime


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)
    bio = models.TextField(max_length=500, null=True, blank=True)
    user_icon = models.ImageField(null=True, blank=True, upload_to='images/')
    country_code = CountryField(blank_label='(select country)')


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Merchants(models.Model):
    id = models.AutoField(primary_key=True)
    merchant_name = models.CharField(max_length=100)
    merchant_description = models.CharField(max_length=200, default="input merchant description")
    country_code = CountryField(blank_label='(select country)')
    created_at = models.DateTimeField(default=datetime.now)
    admin_id = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="user_profile",
        db_column='admin_id',
        default=1
    )


class PropertyType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=50)
    images = models.ImageField(upload_to='property_type/')
    merchant_id = models.ForeignKey(
        Merchants,
        on_delete=models.CASCADE,
        related_name="merchant_information",
        db_column='merchant_id'
    )


class Properties(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    images = models.ImageField(upload_to='properties/')
    merchant_id = models.ForeignKey(
        Merchants,
        on_delete=models.CASCADE,
        related_name="merchant_details",
        db_column='merchant_id'
    )
    property_type_id = models.ForeignKey(
        PropertyType,
        on_delete=models.CASCADE,
        related_name="property_type_information",
        db_column='property_type_id'
    )
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='KES')
    status = models.CharField(max_length=50, choices=[
        ("booked", "booked"),
        ("available", "available")
    ])
    created_at = models.DateTimeField()
    location = CountryField(blank_label='(Select Country')


class Orders(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="user_information",
        db_column='user_id'
    )
    status = models.CharField(max_length=50, choices=[
        ("paid", "paid"),
        ("unpaid", "unpaid")
    ])
    created_at = models.DateTimeField()


class OrderItems(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE, related_name="order_details")
    property_id = models.ForeignKey(
        Properties,
        on_delete=models.CASCADE,
        related_name="property_details",
        db_column='property_id'
    )
    start_of_stay = models.DateTimeField(default=datetime.now)
    end_of_stay = models.DateTimeField(default=datetime.now)
