class Image(models.Model):
    name = models.CharField(max_length=200)
    full = models.FileField()
    thumb = models.FileField()

class Album(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    slug = models.SlugField()

class ImagePlacementInAlbum(models.Model):
    image = models.ForeignKey(Image)
    album = models.ForeignKey(Album)
    caption = models.CharField(max_length=200)
    order = models.IntegerField()