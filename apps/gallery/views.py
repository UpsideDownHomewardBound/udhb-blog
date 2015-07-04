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

    data = request.POST or None

    form_set = PlacementFormSet(data, queryset=album.placements.all())

    valid = form_set.is_valid()

    for form in form_set:
        form.image_form = ImageForm(data,
                                    instance=form.instance.image,
                                    prefix=form.instance.image.id)

        valid = valid and form.image_form.is_valid()

    if valid:
        form_set.save()

        for form in form_set:
            form.image_form.save()


    return render(request, "gallery-edit-album.html",
                  {'album': album,
                   'form_set': form_set})