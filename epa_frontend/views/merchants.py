from datetime import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import redirect, render

from epa_frontend.forms.authentication_forms import MerchantForm
from epa_frontend.models import Merchants, EventsType, Events


@login_required
def create_merchant(request):
    current_user = request.user
    current_user_merchants = Merchants.objects.filter(admin_id=current_user.profile.id)
    current_merchant = [e for e in current_user_merchants]
    events_types = EventsType.objects.all()
    if request.method == 'POST':
        merchant_form = MerchantForm(request.POST)

        if merchant_form.is_valid():
            merchant_form.user_profile_id = current_user.id
            merchant_form.created_at = datetime.now
            merchant_form.save()
            messages.success(request, 'The new merchant has been created succesfully')
            return redirect('view_merchant', pk=current_merchant[0].id)
        else:
            messages.error(request, 'please correct the mistakes below')
    else:
        merchant_form = MerchantForm(request.POST)
    return render(request, 'merchants/new_merchant.html', {
        "merchant_form": merchant_form,
        "events_types": events_types,
        "current_merchants": current_user_merchants
    })


@login_required
def update_merchant(request, pk):
    current_user = request.user
    current_user_merchants = Merchants.objects.filter(admin_id=current_user.profile.id, id=pk)
    current_merchant = [e for e in current_user_merchants]
    events_types = EventsType.objects.all()
    # print(current_merchant[0].merchant_name)
    if request.method == 'POST':
        merchant_form = MerchantForm(request.POST, instance=current_merchant[0])
        if merchant_form.is_valid():
            merchant_form.save()
            messages.success(request, 'Your merchant was successfully updated!')
            return redirect('view_merchant', pk=current_merchant[0].id)
        else:
            messages.error(request, 'Please fix the errors below!')
    else:
        merchant_form = MerchantForm(instance=current_merchant[0])
    return render(request, 'merchants/update_merchant.html', {
        "merchant_form": merchant_form,
        "events_types": events_types,
        "current_merchant": current_merchant[0]
    })


def view_merchant(request, pk):
    current_user = request.user
    user_creation_form = UserCreationForm()
    user_authentication_form = AuthenticationForm()
    merchant = Merchants.objects.get(pk=pk)
    events = Events.objects.filter(merchant_id=merchant.id)
    events_types = EventsType.objects.all()
    return render(request, 'merchants/merchant.html', {
        "merchant": merchant,
        "events": events,
        "user_authentication_form": user_authentication_form,
        "user_creation_form": user_creation_form,
        "events_types": events_types,
        "current_user": current_user
    })


def view_merchants(request):
    current_user = request.user
    user_creation_form = UserCreationForm()
    user_authentication_form = AuthenticationForm()
    merchants = Merchants.objects.all()
    events_types = EventsType.objects.all()
    return render(request, 'merchants/merchants.html', {
        "merchants": merchants,
        "user_authentication_form": user_authentication_form,
        "user_creation_form": user_creation_form,
        "events_types": events_types,
        "current_user": current_user
    })
