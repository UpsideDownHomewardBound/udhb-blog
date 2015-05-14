from django.contrib import admin
from apps.labor.models import ContractionEvent, LaborAnnouncement


class LaborAnnoucementAdmin(admin.ModelAdmin):
    pass


class ContractionEventAdmin(admin.ModelAdmin):
    pass


admin.site.register(LaborAnnouncement, LaborAnnoucementAdmin)
admin.site.register(ContractionEvent, ContractionEventAdmin)