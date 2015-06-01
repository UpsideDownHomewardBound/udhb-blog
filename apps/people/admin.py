from django.contrib import admin
from apps.people.models import PhoneNumber


class PhoneNumberAdmin(admin.ModelAdmin):
    pass

admin.site.register(PhoneNumber, PhoneNumberAdmin)


