from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from apps.gallery.models import Album, ImagePlacementInAlbum, Image
from django.forms.models import modelformset_factory, modelform_factory, ModelForm


def gallery(request):
    return render(request,
                  "gallery.html",
                  )


def album_display(request, album_slug):
    album = Album.objects.get(slug=album_slug)
    return render(request,
                  "gallery-album.html",
                  {'album': album,
                   'image_id': request.GET.get('image', None)
                   },
                  )


PlacementFormSet = modelformset_factory(ImagePlacementInAlbum,
                                        extra=0,
                                        fields=['caption', 'order', 'featured'])


class ImageForm(ModelForm):

    class Meta:
        model = Image
        fields = ['name', 'datetime_taken']


class AlbumForm(ModelForm):

    class Meta:
        model = Album
        fields = ['name']


def edit_album(request, album_slug):
    album = Album.objects.get(slug=album_slug)

    data = request.POST or None

    form_set = PlacementFormSet(data, queryset=album.placements.all())

    valid = form_set.is_valid()

    album_form = AlbumForm(data,
                           instance=album,
                           prefix="album_form")

    for form in form_set:
        order_widget = form.fields['order'].widget
        order_widget.attrs['class'] = "order_input"
        order_widget.is_hidden = True
        form.image_form = ImageForm(data,
                                    instance=form.instance.image,
                                    prefix=form.instance.image.id)

        valid = valid and form.image_form.is_valid() and album_form.is_valid()

    if valid:
        album_form.save()
        form_set.save()

        for form in form_set:
            form.image_form.save()


    return render(request, "gallery-edit-album.html",
                  {'album_form': album_form,
                   'form_set': form_set})