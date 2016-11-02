# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Person, Project, ProjectPhoto, Statut, ZonageINSEE, Commune, Departement, Region, ContexteCommune, TypeOperation, Vocation, LabelEcoQuartier, Procedure, Charte, DREALStringer
from .models import CommissionNationale2009, CommissionNationale2011, CommissionNationale2013, CommissionNationale2014, CommissionNationale2015, CommissionNationale2016


class DREALStringerInline(admin.TabularInline):
    model = DREALStringer


class RegionAdmin(admin.ModelAdmin):
    inlines = [
        DREALStringerInline,
    ]

    actions = ['merge_regions', ]
    def merge_regions(self, request, queryset):
        region = queryset.first()
        if region and queryset.count() > 1:
            regions_to_delete = queryset.exclude(pk=region.id)
            Departement.objects.filter(region__in=regions_to_delete).update(region=region)
            regions_to_delete.delete()


    merge_regions.short_description = u"Réunir des régions"


class CharteAdmin(admin.ModelAdmin):
    list_display = ('region', 'ville', 'nom_ecoquartier', 'code_insee')


class CommuneAdmin(admin.ModelAdmin):
    list_display = ('label', 'code_insee', 'charte_ecoquartier', 'departement')


def make_action(vocation):
    name = 'mark_%s' % vocation
    def action(modeladmin, req, qset):
        for q in qset:
            q.vocations.add(vocation)
    return (name, (action, name, "Mark selected as %s vocation" % vocation))


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('nom', 'engagement', 'creation', 'realisation', 'permis', 'debut', 'livraison', 'achevement', 'complementaire', 'autorisation', 'commune', 'densite_brute', 'densite_brute_logements', 'densite_logements', 'bureaux_activites', 'shon_bureauxm', 'mise_a_jour', 'population', 'littorale', 'montagne', 'candidat_label', 'superficieha', 'surface_nonbatie', 'is_eau', 'is_dechets', 'is_biodiversite', 'is_mobilite', 'is_sobriete_energetique_et_energie_renouvelable', 'is_densite_et_formes_urbaines', 'is_ecoconstruction', 'is_demarches_et_processus', 'is_cadre_de_vie_et_usages', 'is_economie_circulaire', 'is_attenuation_changement_climatique', 'is_label_demarche')
    list_filter = ('label_ecoquartier', 'type_operations', 'littorale', 'montagne')

    def get_actions(self, request):
        return dict([make_action(q) for q in Vocation.objects.all()])


class TypeOperationAdmin(admin.ModelAdmin):
    list_display = ('label', 'hide')


class VocationAdmin(admin.ModelAdmin):
    list_display = ('label', 'hide')


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
admin.site.register(TypeOperation, TypeOperationAdmin)
admin.site.register(Vocation, VocationAdmin)
admin.site.register(LabelEcoQuartier)
admin.site.register(Procedure)
admin.site.register(Person)
admin.site.register(Charte, CharteAdmin)
