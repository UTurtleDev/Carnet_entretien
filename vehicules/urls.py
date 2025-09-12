# from django.contrib import admin
from baton.autodiscover import admin
from django.urls import path
# from django.conf import settings
# from django.conf.urls.static import static
from .views import DetailVehiculesView

app_name = 'vehicules'


urlpatterns = [
    # path('', dashboard, name='dashboard'),
    path('detail/<int:pk>/', DetailVehiculesView.as_view(), name='detail'),
    # path('baton/', include('baton.urls')),
]

