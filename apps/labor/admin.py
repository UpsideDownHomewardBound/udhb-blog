from django.contrib import admin


class LaborAnnoucementAdmin(admin.ModelAdmin):
    pass


class ContractionAdmin(admin.ModelAdmin):
    pass


admin.site.register(LaborAnnoucementAdmin)
admin.site.register(ContractionAdmin)