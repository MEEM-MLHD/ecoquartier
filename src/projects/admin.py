from django.contrib import admin


from .models import Project, ProjectPhoto, Statut, ZonageINSEE, Commune, Departement, Region, ContexteCommune, TypeOperation, Vocation, LabelEcoQuartier, Procedure, Charte


class CharteAdmin(admin.ModelAdmin):
    list_display = ('region', 'ville', 'nom_ecoquartier', 'code_insee')


class CommuneAdmin(admin.ModelAdmin):
    list_display = ('label', 'code_insee', 'charte_ecoquartier', 'departement')


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('nom', 'commune', 'mise_a_jour', 'population', 'littorale', 'montagne', 'candidat_label', 'superficieha', 'surface_nonbatie', 'eau', 'dechets', 'biodiversite', 'mobilite', 'sobriete_energetique_et_energie_renouvelable', 'densite_et_formes_urbaines', 'ecoconstruction', 'autres', 'demarches_et_processus', 'cadre_de_vie_et_usages')


admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectPhoto)
admin.site.register(Statut)
admin.site.register(ZonageINSEE)
admin.site.register(Commune, CommuneAdmin)
admin.site.register(Departement)
admin.site.register(Region)
admin.site.register(ContexteCommune)
admin.site.register(TypeOperation)
admin.site.register(Vocation)
admin.site.register(LabelEcoQuartier)
admin.site.register(Procedure)
admin.site.register(Charte, CharteAdmin)
