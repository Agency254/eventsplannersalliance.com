from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render

from epa_frontend.models import Events, EventsType, Merchants


def view_events(request):
    events = Events.objects.all()
    user_form = UserCreationForm()
    user_authentication_form = AuthenticationForm()
    events_types = EventsType.objects.all()
    return render(request, 'events/events.html', {
        "events": events,
        "user_creation_form": user_form,
        "user_authentication_form": user_authentication_form,
        "events_types": events_types,
    })


def view_event(request, pk):
    event = Events.objects.get(pk=pk)
    print(event.merchant_id)
    # merchant = Merchants.objects.filter(pk=event.merchant_id)
    user_form = UserCreationForm()
    user_authentication_form = AuthenticationForm()
    events_types = EventsType.objects.all()
    return render(request, 'events/event.html', {
        "event": event,
        # "merchant": merchant,
        "user_creation_form": user_form,
        "user_authentication_form": user_authentication_form,
        "events_types": events_types,
    })


@login_required
def create_event(request):
    current_user = request.user
    merchant = Merchants.objects.filter(admin_id=current_user.id)
    events_types = EventsType.objects.all()
    return render(request, 'events/new_event.html', {
        "events_types": events_types,
    })


@login_required
def publish_event(request):
    current_user = request.user
    merchant = Merchants.objects.filter(admin_id=current_user.id)
    events_types = EventsType.objects.all()
    return render(request, 'events/new_event.html', {
        "events_types": events_types,
    })


@login_required
def view_event_dashboard(request, pk):
    event = Events.objects.get(pk=pk)
    print(event.merchant_id)
    # merchant = Merchants.objects.filter(pk=event.merchant_id)
    user_form = UserCreationForm()
    user_authentication_form = AuthenticationForm()
    events_types = EventsType.objects.all()
    return render(request, 'events/event_dashboard.html', {
        "event": event,
        # "merchant": merchant,
        "user_creation_form": user_form,
        "user_authentication_form": user_authentication_form,
        "events_types": events_types,
    })
