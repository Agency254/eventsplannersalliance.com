from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField
from djmoney.models.fields import MoneyField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)
    bio = models.TextField(max_length=500, null=True, blank=True)
    user_icon = models.ImageField(null=True, blank=True)
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
    country_code = CountryField(blank_label='(select country)')
    created_at = models.DateTimeField()
    admin_id = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="user_profile")


class Properties(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    images = models.ImageField()
    property_type = models.CharField(max_length=30) #eg mansion, villa, bungallow
    merchant_id = models.ForeignKey(Merchants, on_delete=models.CASCADE, related_name="merchant_details")
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='KES')
    status = models.CharField(max_length=50, choices=[
        ("booked", "booked"),
        ("available", "available")
    ])
    created_at = models.DateTimeField()


class Orders(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="user_information")
    status = models.CharField(max_length=50, choices=[
        ("paid", "paid"),
        ("unpaid", "unpaid")
    ])
    created_at = models.DateTimeField()


class OrderItems(models.Model):
    order_id = models.ForeignKey(Orders, on_delete=models.CASCADE, related_name="order_details")
    property_id = models.ForeignKey(Properties, on_delete=models.CASCADE, related_name="property_details")
    duration_of_stay = models.DateTimeField()
