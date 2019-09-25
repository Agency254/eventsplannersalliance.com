from datetime import datetime
from django import forms
from django.contrib.auth.models import User
from django_countries.fields import CountryField

from epa_frontend.models import Profile, Merchants


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('email', 'bio', 'user_icon', 'country_code')


class MerchantForm(forms.ModelForm):
    merchant_name = forms.CharField(max_length=100)
    merchant_description = forms.CharField(max_length=200)
    country_code = CountryField(blank_label='(select country)')
    # admin_id = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    # created_at = forms.DateTimeField(widget=forms.HiddenInput(), initial=datetime.now, label=False)

    class Meta:
        model = Merchants
        fields = ('merchant_name', 'merchant_description', 'country_code', 'user_profile_id', 'created_at')
        exclude = ('user_profile_id', 'created_at')
