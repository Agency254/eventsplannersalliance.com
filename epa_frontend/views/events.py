from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.urls import reverse

from epa_frontend.models import Events, EventsType, Merchants


def view_events(request):
    events = Events.get_published_events()
    user_form = UserCreationForm()
    user_authentication_form = AuthenticationForm()
    events_types = EventsType.objects.all()
    return render(request, 'events/events.html', {
        "events": events,
        "user_creation_form": user_form,
        "user_authentication_form": user_authentication_form,
        "events_types": events_types,
    })


def view_event(request, slug):
    event = Events.objects.get(slug=slug)
    # merchant = Merchants.objects.filter(pk=event.merchant_id)
    user_form = UserCreationForm()
    user_authentication_form = AuthenticationForm()
    events_types = EventsType.objects.filter(event_type_information__published=True)
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
def edit_event(request):
    current_user = request.user
    merchant = Merchants.objects.filter(admin_id=current_user.id)
    events_types = EventsType.objects.all()
    return render(request, 'events/new_event.html', {
        "events_types": events_types,
    })


@login_required
def publish_event(request, slug):
    # TODO: Send SMS when event is published
    event = Events.objects.get(slug=slug)
    event.published = True
    event.save(update_fields=['published'])
    messages.success(request, 'Congratulations, The event has been published!')
    nexxt = request.GET.get('next', reverse('index'))
    return redirect(nexxt)


@login_required
def un_publish_event(request, slug):
    # TODO: Send SMS when event is unpublished
    event = Events.objects.get(slug=slug)
    event.published = False
    event.save(update_fields=['published'])
    messages.success(request, 'Congratulations, The event has been un published!')
    nexxt = request.GET.get('next', reverse('index'))
    return redirect(nexxt)


@login_required
def view_event_dashboard(request, slug):
    event = Events.objects.get(slug=slug)
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
