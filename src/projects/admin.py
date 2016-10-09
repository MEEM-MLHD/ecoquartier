from django.contrib import admin


from .models import Person, Project, ProjectPhoto, Statut, ZonageINSEE, Commune, Departement, Region, ContexteCommune, TypeOperation, Vocation, LabelEcoQuartier, Procedure, Charte, DREALStringer
from .models import CommissionNationale2009, CommissionNationale2011, CommissionNationale2013, CommissionNationale2014, CommissionNationale2015, CommissionNationale2016


class DREALStringerInline(admin.TabularInline):
    model = DREALStringer


class RegionAdmin(admin.ModelAdmin):
	inlines = [
        DREALStringerInline,
    ]


class CharteAdmin(admin.ModelAdmin):
    list_display = ('region', 'ville', 'nom_ecoquartier', 'code_insee')


class CommuneAdmin(admin.ModelAdmin):
    list_display = ('label', 'code_insee', 'charte_ecoquartier', 'departement')


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('nom', 'valeur_i1', 'engagement', 'creation', 'realisation', 'permis', 'debut', 'livraison', 'achevement', 'complementaire', 'autorisation', 'commune', 'densite_brute', 'densite_brute_logements', 'densite_logements', 'bureaux_activites', 'shon_bureauxm', 'vocation', 'type_operation', 'mise_a_jour', 'population', 'littorale', 'montagne', 'candidat_label', 'superficieha', 'surface_nonbatie', 'is_eau', 'is_dechets', 'is_biodiversite', 'is_mobilite', 'is_sobriete_energetique_et_energie_renouvelable', 'is_densite_et_formes_urbaines', 'is_ecoconstruction', 'is_demarches_et_processus', 'is_cadre_de_vie_et_usages', 'is_economie_circulaire', 'is_attenuation_changement_climatique', 'is_label_demarche')
    list_filter = ('vocation', 'type_operation', 'littorale', 'montagne')


admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectPhoto)
admin.site.register(CommissionNationale2009)
admin.site.register(CommissionNationale2011)
admin.site.register(CommissionNationale2013)
admin.site.register(CommissionNationale2014)
admin.site.register(CommissionNationale2015)
admin.site.register(CommissionNationale2016)
admin.site.register(Statut)
admin.site.register(ZonageINSEE)
admin.site.register(Commune, CommuneAdmin)
admin.site.register(Departement)
admin.site.register(Region, RegionAdmin)
admin.site.register(ContexteCommune)
admin.site.register(TypeOperation)
admin.site.register(Vocation)
admin.site.register(LabelEcoQuartier)
admin.site.register(Procedure)
admin.site.register(Person)
admin.site.register(Charte, CharteAdmin)
