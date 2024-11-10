from django.urls import path

from cosmos.apps import CosmosConfig
from cosmos.views import slider_view

app_name = CosmosConfig.name

urlpatterns = [
    path('slider/', slider_view, name='slider'),
]
