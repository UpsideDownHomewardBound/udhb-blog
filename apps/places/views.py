from .models import Place
from django.shortcuts import render


def places(request):
    top_level_places = Place.objects.filter(within__isnull=True)
    context_dict = {'places': top_level_places}
    response = render(request, "places.html", context_dict)
    return response
