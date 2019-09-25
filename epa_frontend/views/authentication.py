from datetime import datetime
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.shortcuts import render, redirect

from epa_frontend.forms.authentication_forms import UserForm, ProfileForm, MerchantForm


def signup(request):
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
    return render(request, 'registration/signup.html', {'user_creation_form': form})


@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return redirect('view_profile')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'registration/update_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


def view_profile(request):
    current_user = request.user
    current_user_profile = current_user.profile
    return render(request, 'registration/profile.html', {
        "user": current_user,
        "profile": current_user_profile
    })


@login_required
def create_merchant(request):
    current_user = request.user
    print(current_user.id)
    if request.method == 'POST':
        merchant_form = MerchantForm(request.POST)

        if merchant_form.is_valid():
            merchant_form.user_profile_id = current_user.id
            merchant_form.created_at = datetime.now
            merchant_form.save()
            messages.success(request, ('The new merchant has been created succesfully'))
            return redirect('properties')
        else:
            messages.error(request, 'please correct the mistakes below')
    else:
        merchant_form = MerchantForm(request.POST)
    return render(request, 'registration/merchant_creation.html', {
        "merchant_form": merchant_form
    })
