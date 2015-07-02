from django.contrib import admin
from apps.labor.models import ContractionEvent, LaborAnnouncement, PhoneNumberToInform


class LaborAnnoucementAdmin(admin.ModelAdmin):
    pass


class ContractionEventAdmin(admin.ModelAdmin):
    pass


class InformedAdmin(admin.ModelAdmin):
    pass


admin.site.register(LaborAnnouncement, LaborAnnoucementAdmin)
admin.site.register(ContractionEvent, ContractionEventAdmin)
admin.site.register(PhoneNumberToInform, InformedAdmin)