# from django.contrib import admin
from baton.autodiscover import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import dashboard, dashboardView

app_name = 'dashboard'


urlpatterns = [
    # path('', dashboard, name='dashboard'),
    path('', dashboardView.as_view(), name='dashboard'),
    path('baton/', include('baton.urls')),
]

# Pour voir les fichiers uploader en mode developpement
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)