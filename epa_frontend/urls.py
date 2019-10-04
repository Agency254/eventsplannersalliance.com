from django.conf.urls import url
from django.urls import path, include

from epa_frontend.views import views, authentication, merchants, events, events_type

urlpatterns = [
    url('^$', views.home, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', authentication.view_profile, name='view_profile'),
    path('accounts/profile/update/', authentication.update_profile, name='update_profile'),
    path('accounts/signup/', authentication.signup, name='signup'),
    path('accounts/login/', authentication.login, name='login'),
    path('merchants/new/', merchants.create_merchant, name='create_merchant'),
    path('merchants/', merchants.view_merchants, name='view_merchants'),
    path('merchant/<int:pk>/', merchants.view_merchant, name='view_merchant'),
    path('merchant/<int:pk>/update/', merchants.update_merchant, name='update_merchant'),
    path('events/', events.view_events, name='view_events'),
    path('events/new/', events.create_event, name='create_events'),
    path('about/', views.view_about, name='view_about'),
    path('event/<int:pk>/', events.view_event, name='view_event'),
    path('event/<int:pk>/dashboard/', events.view_event_dashboard, name='view_event_dashboard'),
    path('event-type/<int:pk>/', events_type.view_event_type, name='view_event_type'),
    path('event-type/new/', events_type.create_event_type, name='create_event_type'),
]
