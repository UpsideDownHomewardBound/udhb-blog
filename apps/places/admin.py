from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from .models import Place


admin.site.register(Place)
