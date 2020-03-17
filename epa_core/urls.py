from django.contrib import admin
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.urls import path, include

from epa_core import settings

urlpatterns = [
    path("", include("epa_frontend.urls")),
    path("", include("epa_api.urls")),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
