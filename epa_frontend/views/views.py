from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import transaction
from django.db.models import F
from django.shortcuts import render, redirect

from epa_frontend.forms.authentication_forms import UserForm, ProfileForm
from epa_frontend.models import Properties, PropertyType


def home(request):
    user_creation_form = UserCreationForm()
    user_authentication_form = AuthenticationForm()
    profile_form = ProfileForm()
    current_user = User.username
    property_types = PropertyType.objects.all()
    properties = Properties.objects.all()
    return render(request, 'index.html', {
        "profile_form": profile_form,
        "user_creation_form": user_creation_form,
        "user_authentication_form": user_authentication_form,
        "current_user": current_user,
        "property_types": property_types,
        "properties": properties
    })


def view_properties(request):
    properties = Properties.objects.all()
    user_form = UserCreationForm()
    user_authentication_form = AuthenticationForm()
    return render(request, 'properties_and_property_type/properties.html', {
        "properties": properties,
        "user_creation_form": user_form,
        "user_authentication_form": user_authentication_form,
    })
