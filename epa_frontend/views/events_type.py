from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render

from epa_frontend.models import Merchants, EventsType, Events


@login_required
def create_event_type(request):
    current_user = request.user
    merchant = Merchants.objects.filter(admin_id=current_user.id)
    events_types = EventsType.objects.all()
    return render(request, 'events_types/new_event_type.html', {
        "events_types": events_types,
    })


@login_required
def update_event_type(request, pk):
    current_user = request.user
    merchant = Merchants.objects.filter(admin_id=current_user.id)
    user_form = UserCreationForm()
    user_authentication_form = AuthenticationForm()
    events_types = EventsType.objects.all()
    return render(request, 'events_types/events_type.html', {
        "event_type": events_types,
        "user_creation_form": user_form,
        "user_authentication_form": user_authentication_form,
        "events_types": events_types,
    })


def view_event_type(request, pk):
    event_type = EventsType.objects.get(pk=pk)
    events = Events.objects.filter(event_type_id=event_type.id, published=True)
    user_form = UserCreationForm()
    user_authentication_form = AuthenticationForm()
    events_types = EventsType.objects.all()
    return render(request, 'events_types/events_type.html', {
        "event_type": event_type,
        "events": events,
        "user_creation_form": user_form,
        "user_authentication_form": user_authentication_form,
        "events_types": events_types,
    })
