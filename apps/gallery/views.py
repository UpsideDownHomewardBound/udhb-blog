from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from apps.gallery.models import Album, ImagePlacementInAlbum, Image
from django.forms.models import modelformset_factory, modelform_factory, ModelForm


def gallery(request):
    return render(request, "gallery.html")


def album_display(request, album_slug):
    album = Album.objects.get(slug=album_slug)
    return render(request, "gallery-album.html", {'album': album})


PlacementFormSet = modelformset_factory(ImagePlacementInAlbum,
                                        extra=0,
                                        fields=['caption', 'order'])


class ImageForm(ModelForm):

    class Meta:
        model = Image
        fields = ['name']

def edit_album(request, album_slug):
    album = Album.objects.get(slug=album_slug)


    if request.POST:
        form_set = PlacementFormSet(request.POST, queryset=album.placements.all())
    else:
        form_set = PlacementFormSet(queryset=album.placements.all())

    for form in form_set:
        form.image_form = ImageForm(request.POST,
                                    instance=form.instance.image,
                                    prefix=form.instance.image.id)

        if not form.is_valid():
            print form


    return render(request, "gallery-edit-album.html",
                  {'album': album,
                   'form_set': form_set})