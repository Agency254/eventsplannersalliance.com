from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail, BadHeaderError
from django.db import transaction
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from epa_frontend.forms.authentication_forms import UserForm, ProfileForm
from epa_frontend.models import EventsType, Profile


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
    # TODO: Implement email verification on profile update!
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


def password_reset(request):
    current_site = get_current_site(request)
    print(current_site)
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = Profile.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "registration/password_reset/password_reset_email.html"
                    c = {
                        "email": user.email,
                        'domain': current_site.domain,
                        'site_name': 'eventsplanners',
                        "uid": urlsafe_base64_encode(force_bytes(user.user.pk)),
                        'token': default_token_generator.make_token(user.user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'karanu.newton@students.jkuat.ac.ke', [user.email],
                                  fail_silently=False)
                    except BadHeaderError:

                        return HttpResponse('Invalid header found.')

                    messages.success(request, 'A message with reset password instructions has been sent to your inbox.')
                    return redirect("index")
            messages.error(request, 'An invalid email has been entered.')
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="registration/password_reset/password_reset.html",
                  context={"password_reset_form": password_reset_form})
