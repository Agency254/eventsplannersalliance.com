from django import forms
from django.contrib.auth.models import User

from epa_frontend.models import Profile, Merchants, Properties, Orders


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('email', 'bio', 'user_icon', 'country_code')
