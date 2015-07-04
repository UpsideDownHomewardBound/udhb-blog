from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt

from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin

from mezzanine.core.views import direct_to_template

import mezzanine_pagedown.urls
from apps.labor.views import BirthLine
from apps.people.phone import PrimaryPhoneLine

admin.autodiscover()

# Add the urlpatterns for any custom Django applications here.
# You can also change the ``home`` view to add your own functionality
# to the project's homepage.

urlpatterns = i18n_patterns("",
    # Change the admin prefix here to use an alternate URL for the
    # admin interface, which would be marginally more secure.
    ("^admin/", include(admin.site.urls)),
)

urlpatterns += patterns('',

     url("^places/$", "apps.places.views.places", name="places"),

     url("^gallery/$", "apps.gallery.views.gallery", name="gallery"),
     url("^gallery/(?P<album_slug>[-\w]+)/$", "apps.gallery.views.album_display", name="album_display"),
     url("^gallery/edit/(?P<album_slug>[-\w]+)/$", "apps.gallery.views.edit_album", name="edit_album"),

     url("^$", "mezzanine.blog.views.blog_post_list", name="home"),
     url("^labor/birth_phone_line/(?P<phase_name>\w+)/$",
         csrf_exempt(BirthLine.as_view()),
         name=BirthLine.name
         ),

    url("^phone/primary_line/(?P<phase_name>\w+)/$",
         csrf_exempt(PrimaryPhoneLine.as_view()),
         name=PrimaryPhoneLine.name
         ),

    # MEZZANINE'S URLS
    # ----------------
    # ADD YOUR OWN URLPATTERNS *ABOVE* THE LINE BELOW.
    # ``mezzanine.urls`` INCLUDES A *CATCH ALL* PATTERN
    # FOR PAGES, SO URLPATTERNS ADDED BELOW ``mezzanine.urls``
    # WILL NEVER BE MATCHED!

    # If you'd like more granular control over the patterns in
    # ``mezzanine.urls``, go right ahead and take the parts you want
    # from it, and use them directly below instead of using
    # ``mezzanine.urls``.
    ("^pagedown/", include(mezzanine_pagedown.urls)),
    ("^", include("mezzanine.urls")),


    # MOUNTING MEZZANINE UNDER A PREFIX
    # ---------------------------------
    # You can also mount all of Mezzanine's urlpatterns under a
    # URL prefix if desired. When doing this, you need to define the
    # ``SITE_PREFIX`` setting, which will contain the prefix. Eg:
    # SITE_PREFIX = "my/site/prefix"
    # For convenience, and to avoid repeating the prefix, use the
    # commented out pattern below (commenting out the one above of course)
    # which will make use of the ``SITE_PREFIX`` setting. Make sure to
    # add the import ``from django.conf import settings`` to the top
    # of this file as well.
    # Note that for any of the various homepage patterns above, you'll
    # need to use the ``SITE_PREFIX`` setting as well.

    # ("^%s/" % settings.SITE_PREFIX, include("mezzanine.urls"))

)

# Adds ``STATIC_URL`` to the context of error pages, so that error
# pages can use JS, CSS and images.
handler404 = "mezzanine.core.views.page_not_found"
handler500 = "mezzanine.core.views.server_error"
