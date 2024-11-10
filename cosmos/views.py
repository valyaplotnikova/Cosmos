from django.shortcuts import render
from django.views.generic import TemplateView

from cosmos.models import SliderImage


def slider_view(request):
    images = SliderImage.objects.all()
    return render(request, 'cosmos/home.html', {'images': images})
