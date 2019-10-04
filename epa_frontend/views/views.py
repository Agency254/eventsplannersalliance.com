from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render

from epa_frontend.forms.authentication_forms import ProfileForm
from epa_frontend.models import Events, EventsType


def home(request):
    user_creation_form = UserCreationForm()
    user_authentication_form = AuthenticationForm()
    profile_form = ProfileForm()
    current_user = User.username
    events_types = EventsType.objects.all()
    print(events_types)
    events = Events.objects.all()
    return render(request, 'index.html', {
        "profile_form": profile_form,
        "user_creation_form": user_creation_form,
        "user_authentication_form": user_authentication_form,
        "current_user": current_user,
        "events_types": events_types,
        "events": events
    })


def view_about(request):
    user_creation_form = UserCreationForm()
    user_authentication_form = AuthenticationForm()
    profile_form = ProfileForm()
    current_user = User.username
    events_types = EventsType.objects.all()
    events = Events.objects.all()
    return render(request, 'about.html', {
        "profile_form": profile_form,
        "user_creation_form": user_creation_form,
        "user_authentication_form": user_authentication_form,
        "current_user": current_user,
        "events_types": events_types,
        "events": events
    })
