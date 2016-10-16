# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.contrib.gis.db import models
from django.core.urlresolvers import reverse
from django.utils.text import Truncator


class Person(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    mail = models.EmailField()


class Statut(models.Model):
    label = models.CharField(max_length=255)

    def __unicode__(self):
        return self.label


class ZonageINSEE(models.Model):
    label = models.CharField(max_length=255)

    def __unicode__(self):
        return self.label


class Region(models.Model):
    label = models.CharField(max_length=255)
    stringers = models.ManyToManyField(Person, through="DREALStringer")

    def __unicode__(self):
        return self.label


class DREALStringer(models.Model):
    person = models.ForeignKey(Person)
    region = models.ForeignKey(Region)
    order = models.PositiveIntegerField()


class Departement(models.Model):
    label = models.CharField(max_length=255)
    region = models.ForeignKey(Region, null=True)
    stringers = models.ManyToManyField(Person, through="DDTStringer")

    def __unicode__(self):
        return self.label


class DDTStringer(models.Model):
    person = models.ForeignKey(Person)
    departement = models.ForeignKey(Departement)
    order = models.PositiveIntegerField()


class Commune(models.Model):
    label = models.CharField(max_length=255)
    code_insee = models.CharField(max_length=255)
    charte_ecoquartier = models.BooleanField()
    departement = models.ForeignKey(Departement, null=True)

    def __unicode__(self):
        return self.label


class ContexteCommune(models.Model):
    label = models.CharField(max_length=255)

    def __unicode__(self):
        return self.label


class TypeOperation(models.Model):
    label = models.CharField(max_length=255)

    def __unicode__(self):
        return self.label


class Vocation(models.Model):
    label = models.CharField(max_length=255)

    def __unicode__(self):
        return self.label


class LabelEcoQuartier(models.Model):
    label = models.CharField(max_length=255)

    def __unicode__(self):
        return self.label


class Procedure(models.Model):
    label = models.CharField(max_length=255)

    def __unicode__(self):
        return self.label


class Tag(models.Model):
    label = models.CharField(max_length=255)

    def __unicode__(self):
        return self.label

class Project(models.Model):

    owner = models.ForeignKey(User, null=True, blank=True, related_name="owner")
    editors = models.ManyToManyField(User, related_name="editors")

    nom = models.CharField(max_length=255) #
    mise_a_jour = models.DateField(auto_now_add=True) #
    statut = models.ForeignKey(Statut, null=True) #
    zonage_insee = models.ForeignKey(ZonageINSEE, null=True, verbose_name="Zonage INSEE") #
    commune = models.ForeignKey(Commune, null=True) #
    population = models.IntegerField(default=0) #
    description = models.TextField() #
    contexte_commune = models.ForeignKey(ContexteCommune, null=True) #
    littorale = models.BooleanField(default=False) #
    montagne = models.BooleanField(default=False) #
    autres_communes = models.TextField()
    adresse = models.TextField() #
    systeme_projection = models.CharField(max_length=255) #
    coordonnees_geographiques = models.GeometryCollectionField(blank=True, null=True) #
    site = models.TextField() #
    contexte_site = models.TextField() #
    type_operations = models.ManyToManyField(TypeOperation, verbose_name="Type d'opérations") #
    type_operation_autre = models.TextField() #
    vocation = models.ForeignKey(Vocation, null=True) #
    vocation_autre = models.TextField() #
    superficieha = models.FloatField(null=True) #
    surface_nonbatie = models.FloatField(null=True) #
    habitants = models.IntegerField(default=0) #
    logements = models.IntegerField(default=0) #
    shon_logementsm = models.IntegerField(default=0) #
    logements_sociau = models.IntegerField(null=True, blank=True) #
    equipements_publics = models.TextField() #
    shon_equipementsm = models.IntegerField(null=True, blank=True) #
    commerces_services = models.TextField() #
    shon_commercesm = models.IntegerField(null=True, blank=True)
    bureaux_activites = models.TextField()
    shon_bureauxm = models.IntegerField(null=True, blank=True)
    programme_detail = models.TextField() #
    densite_brute = models.IntegerField(null=True, blank=True) #
    densite_brute_logements = models.IntegerField(null=True, blank=True) #
    densite_logements = models.IntegerField(null=True, blank=True) #
    projet_social = models.TextField() #
    economie_circulaire = models.TextField() #


    def is_economie_circulaire(self):
        return True if self.economie_circulaire != '' else False
    is_economie_circulaire.boolean = True
    is_economie_circulaire.short_description = u'économie circulaire'

    attenuation_changement_climatique = models.TextField() #

    def is_attenuation_changement_climatique(self):
        return True if self.attenuation_changement_climatique != '' else False
    is_attenuation_changement_climatique.boolean = True
    is_attenuation_changement_climatique.short_description = u'atténuation du changement climatique'

    label_demarche = models.TextField() #
    def is_label_demarche(self):
        return True if self.label_demarche != '' else False
    is_label_demarche.boolean = True
    is_label_demarche.short_description = u'label démarche'


    participation_2009 = models.BooleanField(default=False) #
    participation_2011 = models.BooleanField(default=False) #
    nomine = models.BooleanField(default=False) #
    laureat = models.BooleanField(default=False) #
    resultats_palmares = models.TextField() #
    candidat_label = models.BooleanField(default=False) #
    annee_candidature = models.IntegerField(null=True, blank=True) #
    label_ecoquartier = models.ForeignKey(LabelEcoQuartier, null=True, verbose_name=u"État d'avancement") #

    @property
    def state(self):
        if self.label_ecoquartier is None:
            return 'none'
        if self.label_ecoquartier.id == 3:
            return 'labeled'
        elif self.label_ecoquartier.id == 2:
            return 'engaged'
        else:
            return 'none'

    annee_label = models.IntegerField(null=True, blank=True) #
    procedure = models.ForeignKey(Procedure, null=True) #
    procedure_detail = models.TextField() #
    aspects_fonciers = models.TextField() #
    etudes_prealables = models.TextField() #
    concertation = models.TextField() #
    collectivite_ou_epci_porteur = models.CharField(max_length=500) #
    maitrise_ouvrage = models.TextField() #
    maitrise_oeuvre = models.TextField() #
    partenariats = models.TextField() #
    opacrations_marquantes = models.TextField() #
    engagement = models.IntegerField(null=True, blank=True) #
    creation = models.IntegerField(null=True, blank=True) #
    realisation = models.IntegerField(null=True, blank=True) #
    autorisation = models.IntegerField(null=True, blank=True) #
    permis = models.IntegerField(null=True, blank=True) #
    debut = models.IntegerField(null=True, blank=True) #
    livraison = models.IntegerField(null=True, blank=True) #
    achevement = models.IntegerField(null=True, blank=True) #
    complementaire = models.IntegerField(null=True, blank=True) #
    coats = models.TextField() #
    sources = models.TextField() #
    sources_details = models.TextField() #
    contact = models.TextField() #
    sites_enlien = models.TextField() #
    documents = models.TextField() #

    eau = models.TextField() #
    dechets = models.TextField() #
    biodiversite = models.TextField() #
    mobilite = models.TextField() #
    sobriete_energetique_et_energie_renouvelable = models.TextField() #
    densite_et_formes_urbaines = models.TextField() #
    ecoconstruction = models.TextField() #
    autres = models.TextField() #
    demarches_et_processus = models.TextField() #
    cadre_de_vie_et_usages = models.TextField() #

    def is_eau(self):
        return True if self.eau != '' else False
    is_eau.boolean = True
    is_eau.short_description = 'eau'

    def is_dechets(self):
        return True if self.dechets != '' else False
    is_dechets.boolean = True
    is_dechets.short_description = 'dechets'

    def is_biodiversite(self):
        return True if self.biodiversite != '' else False
    is_biodiversite.boolean = True
    is_biodiversite.short_description = 'biodiversite'

    def is_mobilite(self):
        return True if self.mobilite != '' else False
    is_mobilite.boolean = True
    is_mobilite.short_description = 'mobilite'

    def is_sobriete_energetique_et_energie_renouvelable(self):
        return True if self.sobriete_energetique_et_energie_renouvelable != '' else False
    is_sobriete_energetique_et_energie_renouvelable.boolean = True
    is_sobriete_energetique_et_energie_renouvelable.short_description = 'sobriete energetique et energie renouvelable'

    def is_densite_et_formes_urbaines(self):
        return True if self.densite_et_formes_urbaines != '' else False
    is_densite_et_formes_urbaines.boolean = True
    is_densite_et_formes_urbaines.short_description = 'densite et formes urbaines'

    def is_ecoconstruction(self):
        return True if self.ecoconstruction != '' else False
    is_ecoconstruction.boolean = True
    is_ecoconstruction.short_description = 'ecoconstruction'

    def is_demarches_et_processus(self):
        return True if self.demarches_et_processus != '' else False
    is_demarches_et_processus.boolean = True
    is_demarches_et_processus.short_description = 'demarches et processus'

    def is_cadre_de_vie_et_usages(self):
        return True if self.cadre_de_vie_et_usages != '' else False
    is_cadre_de_vie_et_usages.boolean = True
    is_cadre_de_vie_et_usages.short_description = 'cadre de vie et usages'

    tags = models.ManyToManyField(Tag)

    commentaires_demarche_et_processus = models.TextField()
    ambition_1 = models.TextField()
    ambition_2 = models.TextField()
    ambition_3 = models.TextField()
    ambition_4 = models.TextField()
    ambition_5 = models.TextField()
    commentaires_cadre_de_vie_et_usages = models.TextField()
    ambition_6 = models.TextField()
    ambition_7 = models.TextField()
    ambition_8 = models.TextField()
    ambition_9 = models.TextField()
    ambition_10 = models.TextField()
    commentaires_developpement_territorial = models.TextField()
    ambition_11 = models.TextField()
    ambition_12 = models.TextField()
    ambition_13 = models.TextField()
    ambition_14 = models.TextField()
    ambition_15 = models.TextField()
    commentaires_environnement_et_climat = models.TextField()
    ambition_16 = models.TextField()
    ambition_17 = models.TextField()
    ambition_18 = models.TextField()
    ambition_19 = models.TextField()
    ambition_20 = models.TextField()
    synthese_demarche_et_processus = models.TextField()
    engagement_1 = models.TextField()
    engagement_2 = models.TextField()
    engagement_3 = models.TextField()
    engagement_4 = models.TextField()
    engagement_5 = models.TextField()
    synthese_cadre_de_vie_et_usages = models.TextField()
    engagement_6 = models.TextField()
    engagement_7 = models.TextField()
    engagement_8 = models.TextField()
    engagement_9 = models.TextField()
    engagement_10 = models.TextField()
    synthese_developpement_territorial = models.TextField()
    engagement_11 = models.TextField()
    engagement_12 = models.TextField()
    engagement_13 = models.TextField()
    engagement_14 = models.TextField()
    engagement_15 = models.TextField()
    synthese_environnement_et_climat = models.TextField()
    engagement_16 = models.TextField()
    engagement_17 = models.TextField()
    engagement_18 = models.TextField()
    engagement_19 = models.TextField()
    engagement_20 = models.TextField()

    indicateur_i1 = models.TextField()
    valeur_i1 = models.TextField()
    indicateur_i2 = models.TextField()
    valeur_i2 = models.TextField()
    indicateur_i3 = models.TextField()
    valeur_i3 = models.TextField()
    indicateur_i4 = models.TextField()
    valeur_i4 = models.TextField()
    indicateur_i5 = models.TextField()
    valeur_i5 = models.TextField()
    indicateur_i6 = models.TextField()
    valeur_i6 = models.TextField()
    indicateur_i7 = models.TextField()
    valeur_i7 = models.TextField()
    indicateur_i8 = models.TextField()
    valeur_i8 = models.TextField()
    indicateur_i9 = models.TextField()
    valeur_i9 = models.TextField()
    indicateur_i10 = models.TextField()
    valeur_i10 = models.TextField()
    indicateur_i11 = models.TextField()
    valeur_i11 = models.TextField()
    indicateur_i12 = models.TextField()
    valeur_i12 = models.TextField()
    indicateur_i13 = models.TextField()
    valeur_i13 = models.TextField()
    indicateur_i14 = models.TextField()
    valeur_i14 = models.TextField()
    indicateur_i15 = models.TextField()
    valeur_i15 = models.TextField()
    indicateur_i16 = models.TextField()
    valeur_i16 = models.TextField()
    indicateur_i17 = models.TextField()
    valeur_i17 = models.TextField()
    indicateur_i18 = models.TextField()
    valeur_i18 = models.TextField()
    indicateur_i19 = models.TextField()
    valeur_i19 = models.TextField()
    indicateur_i20 = models.TextField()
    valeur_i20 = models.TextField()
    indicateur_i21 = models.TextField()
    valeur_i21 = models.TextField()
    indicateur_i22 = models.TextField()
    valeur_i22 = models.TextField()
    indicateur_i23 = models.TextField()
    valeur_i23 = models.TextField()
    indicateur_i24 = models.TextField()
    valeur_i24 = models.TextField()
    indicateur_i25 = models.TextField()
    valeur_i25 = models.TextField()
    indicateur_i26 = models.TextField()
    valeur_i26 = models.TextField()
    indicateur_i27 = models.TextField()
    valeur_i27 = models.TextField()
    indicateur_i28 = models.TextField()
    valeur_i28 = models.TextField()
    indicateur_i29 = models.TextField()
    valeur_i29 = models.TextField()
    indicateur_i30 = models.TextField()
    valeur_i30 = models.TextField()
    indicateur_i31 = models.TextField()
    valeur_i31 = models.TextField()
    indicateur_i32 = models.TextField()
    valeur_i32 = models.TextField()
    indicateur_i33 = models.TextField()
    valeur_i33 = models.TextField()
    indicateur_i34 = models.TextField()
    valeur_i34 = models.TextField()
    indicateur_i35 = models.TextField()
    valeur_i35 = models.TextField()
    indicateur_i36 = models.TextField()
    valeur_i36 = models.TextField()
    indicateur_i37 = models.TextField()
    valeur_i37 = models.TextField()
    indicateur_i38 = models.TextField()
    valeur_i38 = models.TextField()
    indicateur_i39 = models.TextField()
    valeur_i39 = models.TextField()
    indicateur_i40 = models.TextField()
    valeur_i40 = models.TextField()
    indicateur_i41 = models.TextField()
    valeur_i41 = models.TextField()
    indicateur_i42 = models.TextField()
    valeur_i42 = models.TextField()
    indicateur_i43 = models.TextField()
    valeur_i43 = models.TextField()
    indicateur_i44 = models.TextField()
    valeur_i44 = models.TextField()
    indicateur_i45 = models.TextField()
    valeur_i45 = models.TextField()
    indicateur_i46 = models.TextField()
    valeur_i46 = models.TextField()
    indicateur_i47 = models.TextField()
    valeur_i47 = models.TextField()
    indicateur_i48 = models.TextField()
    valeur_i48 = models.TextField()
    indicateur_i49 = models.TextField()
    valeur_i49 = models.TextField()
    indicateur_i50 = models.TextField()
    valeur_i50 = models.TextField()

    commentaires = models.TextField()

    objects = models.GeoManager()

    @property
    def commune_label(self):
        return self.commune.label

    @property
    def short_description(self):
        return Truncator(self.description).words(50, html=False, truncate=' ...')

    @property
    def feature(self):
        return self.photos[0] if len(self.photos) > 0 else None

    @property
    def photos(self):
        return [photo.photo.url for photo in self.projectphoto_set.exclude(photo__isnull=True)]

    @models.permalink
    def get_absolute_url(self):
        return ('detail', (), {'pk': self.pk})

    @property
    def url(self):
        return reverse('detail', kwargs={'pk':self.id})

    def __unicode__(self):
        if self.commune.departement:
            return "%s (%s, %s)" % (self.nom, self.commune, self.commune.departement.region)
        else:
            return "%s (%s)" % (self.nom, self.commune)


class ProjectPhoto(models.Model):
    project = models.ForeignKey(Project)
    order = models.PositiveIntegerField()
    title = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', max_length=1500)


class Charte(models.Model):
    region = models.TextField()
    ancienne_region = models.TextField()
    n_dept = models.TextField()
    nom_dept = models.TextField()
    code_insee = models.TextField()
    ville = models.TextField()
    commune = models.ForeignKey(Commune, null=True)
    nom_ecoquartier = models.TextField()
    population = models.TextField()
    commune_rurale_ou_urbaine = models.TextField()
    situation_territoriale = models.TextField()
    situation_du_quartier = models.TextField()
    type_d_operation = models.TextField()
    nombre_d_habitants_dans_le_quartier = models.TextField()
    nombre_de_logements = models.TextField()
    nombre_de_logements_sociaux = models.TextField()
    superficie_du_quartier_ha = models.TextField()
    epa = models.TextField()
    anru = models.TextField()
    pnr = models.TextField()
    aap_2009 = models.TextField()
    aap_2011 = models.TextField()
    charte = models.TextField()
    candidat_2013 = models.TextField()
    resultats_2013 = models.TextField()
    candidat_2014 = models.TextField()
    resultats_2014 = models.TextField()
    candidat_2015 = models.TextField()
    resultats_2015 = models.TextField()
    dotation_evaluation = models.TextField()
    commentaires = models.TextField()
    candidat_potentiel_reperage_ad4_2017 = models.TextField()
    candidat_2016 = models.TextField()
    avancement_dans_la_demarche = models.TextField()
    contact_1_mail = models.TextField()
    contact_1_titre = models.TextField()
    contact_1_prenom_nom = models.TextField()
    contact_2_mail = models.TextField()
    contact_2_titre = models.TextField()
    contact_2_prenom_nom = models.TextField()
    contact_3_mail = models.TextField()
    contact_3_titre = models.TextField()
    contact_3_prenom_nom = models.TextField()
    contact_4_mai = models.TextField()
    contact_4_titre = models.TextField()
    contact_4_prenom_nom = models.TextField()
    contact_5_mail = models.TextField()
    contact_5_titre = models.TextField()
    contact_5_prenom_nom = models.TextField()
    contact_6_mail = models.TextField()
    contact_6_titre = models.TextField()
    contact_6_prenom_nom = models.TextField()
    contact_7_mail = models.TextField()
    contact_7_titre = models.TextField()
    contact_7_prenom_nom = models.TextField()


class CommissionNationale2016(models.Model):
    project = models.OneToOneField(Project)
    commission_nationale_cn2016 = models.TextField()
    decision_cn2016 = models.TextField()
    demarche_processus_cn2016 = models.TextField()
    cadre_vie_usage_cn2016 = models.TextField()
    developpement_territorial_cn2016 = models.TextField()
    ressources_climat_cn2016 = models.TextField()
    etat_avancement_cn2016 = models.TextField()
    commission_regionale_cr2016 = models.TextField()
    proposition_cr2016 = models.TextField()
    demarche_processus_cr2016 = models.TextField()
    cadre_vie_usage_cr2016 = models.TextField()
    developpement_territorial_cr2016 = models.TextField()
    ressources_climat_cr2016 = models.TextField()
    etat_avancement_cr2016 = models.TextField()
    avis_triple_expert_te2016 = models.TextField()
    proposition_te2016 = models.TextField()
    expert_interne_ei2016 = models.TextField()
    avis_general_ei2016 = models.TextField()
    expert_externe_ee2016 = models.TextField()
    avis_general_ee2016 = models.TextField()
    expert_territ_et2016 = models.TextField()
    synthese_avis_et2016 = models.TextField()
    synthese_avis_opportunite_dd2016 = models.TextField()


class CommissionNationale2015(models.Model):
    project = models.OneToOneField(Project)
    commission_nationale_cn2015 = models.TextField()
    decision_cn2015 = models.TextField()
    demarche_processus_cn2015 = models.TextField()
    cadre_vie_usage_cn2015 = models.TextField()
    developpement_territorial_cn2015 = models.TextField()
    ressources_climat_cn2015 = models.TextField()
    etat_avancement_cn2015 = models.TextField()
    commission_regionale_cr2015 = models.TextField()
    proposition_cr2015 = models.TextField()
    demarche_processus_cr2015 = models.TextField()
    cadre_vie_usage_cr2015 = models.TextField()
    developpement_territorial_cr2015 = models.TextField()
    ressources_climat_cr2015 = models.TextField()
    etat_avancement_cr2015 = models.TextField()
    avis_triple_expert_te2015 = models.TextField()
    proposition_te2015 = models.TextField()
    expert_interne_ei2015 = models.TextField()
    avis_general_ei2015 = models.TextField()
    expert_externe_ee2015 = models.TextField()
    avis_general_ee2015 = models.TextField()
    expert_territ_et2015 = models.TextField()
    synthese_avis_et2015 = models.TextField()
    synthese_avis_opportunite_dd2015 = models.TextField()


class CommissionNationale2014(models.Model):
    project = models.OneToOneField(Project)
    commission_nationale_cn2014 = models.TextField()
    decision_cn2014 = models.TextField()
    demarche_processus_cn2014 = models.TextField()
    cadre_vie_usage_cn2014 = models.TextField()
    developpement_territorial_cn2014 = models.TextField()
    ressources_climat_cn2014 = models.TextField()
    etat_avancement_cn2014 = models.TextField()
    commission_regionale_cr2014 = models.TextField()
    proposition_cr2014 = models.TextField()
    demarche_processus_cr2014 = models.TextField()
    cadre_vie_usage_cr2014 = models.TextField()
    developpement_territorial_cr2014 = models.TextField()
    ressources_climat_cr2014 = models.TextField()
    etat_avancement_cr2014 = models.TextField()
    avis_triple_expert_te2014 = models.TextField()
    expert_interne_ei2014 = models.TextField()
    avis_general_ei2014 = models.TextField()
    expert_externe_ee2014 = models.TextField()
    avis_general_ee2014 = models.TextField()
    expert_territ_et2014 = models.TextField()
    synthese_avis_et2014 = models.TextField()
    synthese_avis_opportunite_dd2014 = models.TextField()


class CommissionNationale2013(models.Model):
    project = models.OneToOneField(Project)
    demarche_processus_el2013 = models.TextField()
    cadre_vie_usage_el2013 = models.TextField()
    developpement_territorial_el2013 = models.TextField()
    ressources_climat_el2013 = models.TextField()
    synthese_avis_el2013 = models.TextField()
    proposition_el2013 = models.TextField()


class CommissionNationale2011(models.Model):
    project = models.OneToOneField(Project)
    expert_interne_ei2011 = models.TextField()
    avis_general_ei2011 = models.TextField()
    propositions_prix_ei2011 = models.TextField()
    demarche_processus_ei2011 = models.TextField()
    cadre_vie_usage_ei2011 = models.TextField()
    developpement_territorial_ei2011 = models.TextField()
    ressources_climat_ei2011 = models.TextField()
    approche_integree_ei2011 = models.TextField()
    etat_avancement_ei2011 = models.TextField()
    expert_externe_ee2011 = models.TextField()
    avis_general_ee2011 = models.TextField()
    propositions_prix_ee2011 = models.TextField()
    demarche_processus_ee2011 = models.TextField()
    cadre_vie_usage_ee2011 = models.TextField()
    developpement_territorial_ee2011 = models.TextField()
    ressources_climat_ee2011 = models.TextField()
    approche_integree_ee2011 = models.TextField()
    etat_avancement_ee2011 = models.TextField()
    expert_local_el2011 = models.TextField()
    synthese_avis_el2011 = models.TextField()
    propositions_prix_el2011 = models.TextField()
    alerte_el2011 = models.TextField()


class CommissionNationale2009(models.Model):
    project = models.OneToOneField(Project)
    expertise_2009_e2009 = models.TextField()
    avis_e2009 = models.TextField()
    propositions_prix_e2009 = models.TextField()
    etat_avancement_e2009 = models.TextField()
    points_vigilance_e2009 = models.TextField()

