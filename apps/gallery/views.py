from django.shortcuts import render
from apps.gallery.models import Album


def gallery(request):
    return render(request, "gallery.html")


def album_display(request, album_slug):
    album = Album.objects.get(slug=album_slug)
    return render(request, "gallery-album.html", {'album': album})