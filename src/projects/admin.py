from django.contrib import admin


from .models import Project, Statut, ZonageINSEE, Commune, Departement, Region, ContexteCommune, TypeOperation, Vocation, LabelEcoQuartier, Procedure, Charte

class CharteAdmin(admin.ModelAdmin):
    list_display = ('region', 'ville', 'nom_ecoquartier')


admin.site.register(Project)
admin.site.register(Statut)
admin.site.register(ZonageINSEE)
admin.site.register(Commune)
admin.site.register(Departement)
admin.site.register(Region)
admin.site.register(ContexteCommune)
admin.site.register(TypeOperation)
admin.site.register(Vocation)
admin.site.register(LabelEcoQuartier)
admin.site.register(Procedure)
admin.site.register(Charte, CharteAdmin)
