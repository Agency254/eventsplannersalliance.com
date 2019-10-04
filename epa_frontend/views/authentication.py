from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.shortcuts import render, redirect

from epa_frontend.forms.authentication_forms import UserForm, ProfileForm
from epa_frontend.models import EventsType


def signup(request):
    events_types = EventsType.objects.all()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'user_creation_form': form,
        "events_types": events_types,
    })


@login_required
@transaction.atomic
def update_profile(request):
    events_types = EventsType.objects.all()
    print(request.user.profile)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('view_profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'registration/update_profile.html', {
        'user_form': user_form,
        "events_types": events_types,
        'profile_form': profile_form
    })


@login_required
def view_profile(request):
    current_user = request.user
    current_user_profile = current_user.profile
    events_types = EventsType.objects.all()
    return render(request, 'registration/profile.html', {
        "user": current_user,
        "events_types": events_types,
        "profile": current_user_profile
    })
