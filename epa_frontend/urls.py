from django.conf.urls import url
from django.urls import path, include

from epa_frontend.views import views, authentication
urlpatterns = [
    url('^$', views.home, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', authentication.view_profile, name='view_profile'),
    path('accounts/profile/update/', authentication.update_profile, name='update_profile'),
    path('accounts/signup/', authentication.signup, name='signup'),
    path('accounts/login/', authentication.login, name='login'),
]
