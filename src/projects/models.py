# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import date

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

    class Meta:
        ordering = ['label', ]


class Region(models.Model):
    label = models.CharField(max_length=255)
    stringers = models.ManyToManyField(Person, through="DREALStringer")
    code_insee = models.CharField(max_length=255, default="")

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
    code_insee = models.CharField(max_length=255, default="")

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


class HideManager(models.Manager):
    def get_queryset(self):
        return super(HideManager, self).get_queryset().filter(hide=False)


class TypeOperation(models.Model):
    label = models.CharField(max_length=255)
    hide = models.BooleanField(default=False)

    objects = HideManager()

    def __unicode__(self):
        return self.label

    class Meta:
        ordering = ['label', ]


class Vocation(models.Model):
    label = models.CharField(max_length=255)
    hide = models.BooleanField(default=False)

    objects = HideManager()

    class Meta:
        ordering = ['label', ]

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
    hide = models.BooleanField(default=False)

    objects = HideManager()

    def __unicode__(self):
        return self.label

    class Meta:
        ordering = ['label', ]


class Demarche(models.Model):
    label = models.CharField(max_length=255)

    def __unicode__(self):
        return self.label

    class Meta:
        ordering = ['label', ]


class Echelle(models.Model):
    label = models.CharField(max_length=255)

    def __unicode__(self):
        return self.label

engagement_1_help = u'''
<div>
<h5>Les données qualitatives / Décrire votre projet</h5>

<h6>NOTION 1 : DIAGNOSTIC STRATÉGIQUE</h6>

<ol>
<li>Quels diagnostics ont été réalisés,et à quelles échelles ? Quels sont les champs couverts (sociaux,urbains,économiques et environnementaux) ? Quels sont les enjeux identi és pour le projet ?</li>
<li>Comment les diagnostics ont-ils été mobilisés pour dé nir le projet,notamment en prenant en compte la complémentarité avec les caractéristiques des territoires voisins,les ressources locales,les attentes des habitants,usagers et acteurs socio- économiques ?</li>
</ol>

<h6>NOTION 2 : PROGRAMMATION</h6>

<ol>
<li>Comment la programmation intègre-t-elle les enjeux et les besoins des habitants, des usagers et des acteurs socio- économiques identi és dans les diagnostics, dans un souci d’équité ?</li>
<li>En quoi la programmation est-elle en adéquation avec le contexte local ? Exemples : adéquation de la programmation des logements avec les revenus des ménages et les capacités des acteurs économiques et de la collectivité, de la programmation des équipements publics avec la population visée et l’état des équipements existants, de la programmation commerciale avec les besoins et l’offre existante....</li>
<li>Quelles sont les possibilités d’ajustement de la programmation en fonction de l’évolution du contexte économique, politique,réglementaire,social ou climatique ?</li>
</ol>

</div>
'''


engagement_9_help = u'''
<div>
<h5>Les données qualitatives / Décrire votre projet</h5>
<h6>NOTION 1 : INSERTION URBAINE ET PAYSAGÈRE</h6>

<ol>
<li>Comment le projet s’articule-t-il à son environnement urbain et naturel ?
Exemples : perspectives et points de vue, trame viaire, articulation avec les quartiers mitoyens,...</li>
<li>Comment le projet prend-il en compte et exploite-t-il les éléments paysagers présents sur le site ?</li>
</ol>
<h6>NOTION 2 : QUALITÉ URBAINE ET ESPACES PUBLICS</h6>

<ol>
<li>Comment la composition et les formes urbaines participent-elles à la création d’un cadre de vie agréable?
Exemples : maillage, structuration</li>
<li>Quelle importance est accordée aux espaces publics et quels aménagements favorisant la qualité de vie sont proposés dans le projet ?
Exemples : opérations d’espaces publics particulières,intégration de la multifonctionnalité ...</li>
<li>Comment la nature en ville participe-t-elle à la qualité du cadre de vie ?</li>
</ol>

<h6>NOTION 3 : QUALITÉ ET CRÉATIVITÉ ARCHITECTURALE</h6>

<ol>
<li>Comment les îlots et formes bâties participent-ils à une qualité architecturale d’ensemble du projet ?</li>
<li>De quelle manière favorisez-vous la création et la qualité architecturales dans les projets ?</li>
</ol>
<p>
Exemples : projets architecturaux spécifiques, consultation d’équipes mixtes d’architectes-promoteurs-urbanistes, concours d’idées,...
</p>
</div>
'''

context_site_help = u'''
<ul>
<li>La collectivité fait-elle partie d’une intercommunalité ? Si oui, de quel type d’EPCI s’agit-il ? Quel est le nom de cet EPCI ?</li>

<li>Quels sont les éléments de cadrage et de plani cation valables sur le territoire de la collectivité ?</li>

<li>Le périmètre opérationnel de l’EcoQuartier est-il soumis à des orientations d’aménagement ? Si oui, précisez lesquelles.</li>

<li>Le site de l’EcoQuartier est-il inclus dans un périmètre de protection ou dans une zone à enjeux en termes de patrimoine : périmètre de protection autour des monuments historiques ? Plan de Sauvegarde et de Mise en Valeur (PSMV)? Zone de protection du patrimoine architectural et paysager (ZPPAUP) / Aire de valorisation de l’Architecture et du Patrimoine (AVAP) ? Autres : précisez lesquelles.</li>

<li>Le site de l’EcoQuartier est-il inclus dans un périmètre de protection ou dans une zone à enjeux naturels et paysagers : Zone naturelle d’intérêt Ecologique, Faunistique et Floristiques (ZNIEFF) ? NATURA 2000 ? Espace Boisé Classé (EBC) ? Espace Naturel Sensible (ENS) ? Autres : précisez lesquelles.</li>

<li>Le site de l’EcoQuartier est-il inclus dans un périmètre faisant l’objet de conventions particulières : Périmètre Agence Nationale pour la Rénovation Urbaine (ANRU) ? Convention Programme National de Requali cation des Quartiers Anciens Dégradés (PNRQAD) ? Opération Programmée d’Amélioration de l’Habitat (OPAH) ? Zone Franche Urbaine (ZFU) ? Autres : précisez lesquelles ? Le site de l’EcoQuartier est-il soumis à des servitudes particulières ? Si oui, précisez lesquelles.</li>
</ul>
'''


logements_help = u'''
<p>
Quel est le nombre de logements dans l’EcoQuartier ?
<br>
Préciser le nombre total de logements prévus à terme dans l’opération (y compris logements réhabilités ou rénovés, à préciser dans ce cas dans le détail de l’opération)
</p>
'''

class Project(models.Model):

    owner = models.ForeignKey(User, null=True, blank=True, related_name="owner")
    editors = models.ManyToManyField(User, related_name="editors")

    nom = models.CharField(u"Nom de l'ÉcoQuartier", max_length=255) #
    mise_a_jour = models.DateField(auto_now_add=True) #
    statut = models.ForeignKey(Statut, null=True) #
    zonage_insee = models.ForeignKey(ZonageINSEE, null=True, verbose_name="Zonage INSEE") #
    commune = models.ForeignKey(Commune, null=True, verbose_name="Commune principale", help_text=u"Sur quelle commune est situé l'ÉcoQuartier") #
    communes = models.ManyToManyField(Commune, related_name="other_communes") #
    population = models.IntegerField(default=0) #
    description = models.TextField("Description du projet", help_text="10 lignes maximum") #
    contexte_commune = models.ForeignKey(ContexteCommune, null=True) #
    littorale = models.BooleanField(default=False) #
    montagne = models.BooleanField(default=False) #
    autres_communes = models.TextField()
    adresse = models.TextField() #
    systeme_projection = models.CharField(max_length=255) #
    coordonnees_geographiques = models.GeometryCollectionField(blank=True, null=True) #
    site = models.TextField("Caractéristiques initiales du site", help_text=u"Préciser les caractéristiques initiales du site : par exemple, terrains agricoles, site militaire, friches industrielles, quartier d’habitat social...") #
    contexte_site = models.TextField("Contexte du site", help_text=context_site_help) #
    type_operations = models.ManyToManyField(TypeOperation, verbose_name="Type d'opérations") #
    type_operation_autre = models.TextField() #
    vocations = models.ManyToManyField(Vocation) #
    vocation_autre = models.TextField() #
    superficieha = models.FloatField(u"Superficie de l'opération", help_text=u"Quelle est la superficie de l'EcoQuartier ? (ha)", null=True) #
    surface_nonbatie = models.FloatField(u"Surface non bâtie publique", help_text=u"Toute surface non bâtie appartenant au domaine public, notamment voirie, espaces verts, espaces publics", null=True) #
    habitants = models.IntegerField(u"Nombre d'habitants prévus", default=0) #
    logements = models.IntegerField(u"Nombre de logements", help_text=logements_help , default=0) #
    shon_logementsm = models.IntegerField(u"SHON logement", help_text=u"Surface hors œuvre net des logements", default=0) #
    logements_sociau = models.IntegerField(u"Nombre de logements sociaux", help_text=u"", null=True, blank=True) #
    logements_sociaux_detail = models.TextField(u"Logements sociaux détail")
    equipements_publics = models.TextField(u"Détail équipements publics", help_text=u"Précisions sur les équipements publics considérés") #
    shon_equipementsm = models.IntegerField(u"Surface équipements publics", null=True, blank=True) #
    commerces_services = models.TextField(u"Détail commerces et services", help_text=u"Préciser le type de commerces et services programmés dans l'opération") #
    shon_commercesm = models.IntegerField(u"Surface de plancher des commerces et services", null=True, blank=True)
    bureaux_activites = models.TextField(u"Détail bureaux et activités", help_text=u"Préciser le type d'activités prévues dans l'opération")
    shon_bureauxm = models.IntegerField(u"Surface de plancher bureaux et activités", null=True, blank=True)
    programme_detail = models.TextField() #
    densite_brute = models.IntegerField(null=True, blank=True) #
    densite_brute_logements = models.IntegerField(null=True, blank=True) #
    densite_logements = models.IntegerField(null=True, blank=True) #
    projet_social = models.TextField() #
    economie_circulaire = models.TextField() #

    charte = models.FileField(upload_to='charte/%Y/%m/%d/', null=True, blank=True, verbose_name="Charte ÉcoQuartier")
    charte_date = models.DateField(null=True, blank=True)
    demarches = models.ManyToManyField(Demarche, verbose_name=u"Engagement dans d'autres démarches de développement durable")
    echelle = models.ForeignKey(Echelle, null=True, blank=True)

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
            return 'charte'

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
    opacrations_marquantes = models.TextField(u"Opérations marquantes du projet", help_text=u"<i>Si  au  sein  de  l’opération  d’aménagement,  une  ou  plusieurs  constructions  ou  espaces  publics  majeurs  méritent  d’être  remarquées,  vous  pouvez  nous  indiquer  ici  tous  les  éléments  nécessaires  (nom  du  bâtiment  ou  de  l’espace  public,  fonction,  maîtrise  d’ouvrage  et  maîtrise  d’œuvre,  particularités  de  l’opération, autres éléments ou photographies en votre possession...)</i>") #
    engagement = models.IntegerField("Date d'engagement de l'opération", help_text=u"L’année d’engagement de l’opération : année de la première délibération concernant l’opération", null=True, blank=True) #
    creation = models.IntegerField(u"Date de création de la ZAC", help_text=u"L’année de création de la ZAC (si ZAC)", null=True, blank=True) #
    realisation = models.IntegerField(u"Date de réalisation de la ZAC", help_text="Année de réalisation de la ZAC (si ZAC)", null=True, blank=True) #
    autorisation = models.IntegerField(u"Date d'autorisation d'aménager", help_text=u"Année d’autorisation d’aménager (si permis d’aménager)", null=True, blank=True) #
    permis = models.IntegerField(u"Date du permis de construire", help_text=u"année du permis de construire (si opération se limite à un permis ou un permis groupé)", null=True, blank=True) #
    debut = models.IntegerField(u"Date du début des travaux", help_text=u"année du début des travaux", null=True, blank=True) #
    livraison = models.IntegerField(u"Date de livraison des premiers bâtiments",help_text=u"Année de livraison des premiers bâtiments", null=True, blank=True) #
    achevement = models.IntegerField(u"Date d'achèvement de l'opération", help_text=u"Année d’achèvement de l’opération", null=True, blank=True) #
    complementaire = models.IntegerField(u"Date complémentaire", help_text=u"Autre date importante non citée ci-dessus", null=True, blank=True) #
    coats = models.TextField() #
    sources = models.TextField() #
    sources_details = models.TextField() #
    contact = models.TextField() #
    project_manager_lastname = models.CharField("Nom", max_length=255, null=True, blank=True)
    project_manager_firstname = models.CharField("Prénom", max_length=255, null=True, blank=True)
    project_manager_mail = models.EmailField("Mail", max_length=255, null=True, blank=True)
    project_manager_structure = models.CharField("Organisme de rattachement", max_length=255, null=True, blank=True)


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

    tags = models.ManyToManyField(Tag, verbose_name="Points forts du projet")

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
    engagement_1 = models.TextField(help_text=engagement_1_help)
    engagement_2 = models.TextField()
    engagement_3 = models.TextField()
    engagement_4 = models.TextField()
    engagement_5 = models.TextField()
    synthese_cadre_de_vie_et_usages = models.TextField()
    engagement_6 = models.TextField()
    engagement_7 = models.TextField()
    engagement_8 = models.TextField()
    engagement_9 = models.TextField(help_text=engagement_9_help)
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

    @property
    def engagement_1_completed(self):
        fields = ['site', 'contexte_site', 'superficieha', 'surface_nonbatie',  'engagement', 'creation', 'realisation', 'autorisation', 'permis', 'debut', 'livraison', 'achevement', 'complementaire', 'programme_detail', 'etudes_prealables', 'opacrations_marquantes', 'habitants', 'logements', 'shon_logementsm', 'logements_sociau', 'equipements_publics', 'shon_equipementsm', 'commerces_services', 'shon_commercesm', 'bureaux_activites', 'shon_bureauxm', 'engagement_1', ]
        return self.completed(fields)

    @property
    def engagement_2_completed(self):
        fields = ['procedure', 'procedure_detail', 'concertation', 'collectivite_ou_epci_porteur', 'maitrise_ouvrage', 'maitrise_oeuvre', 'partenariats', 'engagement_2']
        return self.completed(fields)

    @property
    def engagement_3_completed(self):
        fields = ['coats', 'engagement_3']
        return self.completed(fields)

    @property
    def engagement_4_completed(self):
        fields = ['engagement_4']
        return self.completed(fields)

    @property
    def engagement_5_completed(self):
        fields = ['engagement_5']
        return self.completed(fields)

    @property
    def dimension_1_completed(self):
        values = [self.engagement_1_completed, self.engagement_2_completed, self.engagement_3_completed, self.engagement_4_completed, self.engagement_5_completed]
        return sum(values)

    @property
    def engagement_6_completed(self):
        fields = ['aspects_fonciers', 'densite_brute', 'densite_brute_logements', 'densite_logements', 'surface_nonbatie', 'engagement_6']
        return self.completed(fields)

    @property
    def engagement_7_completed(self):
        fields = ['habitants', 'logements', 'shon_logementsm', 'logements_sociau', 'engagement_7']
        return self.completed(fields)

    @property
    def engagement_8_completed(self):
        fields = ['coats', 'engagement_8']
        return self.completed(fields)

    @property
    def engagement_9_completed(self):
        fields = ['opacrations_marquantes', 'engagement_9']
        return self.completed(fields)

    @property
    def engagement_10_completed(self):
        fields = ['contexte_site', 'engagement_10']
        return self.completed(fields)

    @property
    def dimension_2_completed(self):
        values = [self.engagement_6_completed, self.engagement_7_completed, self.engagement_8_completed, self.engagement_9_completed, self.engagement_10_completed, ]
        return sum(values)

    @property
    def engagement_11_completed(self):
        fields = ['equipements_publics', 'shon_equipementsm', 'commerces_services', 'shon_commercesm', 'bureaux_activites', 'shon_bureauxm', 'engagement_11']
        return self.completed(fields)

    @property
    def engagement_12_completed(self):
        fields = ['equipements_publics', 'shon_equipementsm', 'commerces_services', 'shon_commercesm', 'bureaux_activites', 'shon_bureauxm', 'engagement_12']
        return self.completed(fields)

    @property
    def engagement_13_completed(self):
        fields = ['engagement_13']
        return self.completed(fields)

    @property
    def engagement_14_completed(self):
        fields = ['engagement_14']
        return self.completed(fields)

    @property
    def engagement_15_completed(self):
        fields = ['engagement_15']
        return self.completed(fields)

    @property
    def dimension_3_completed(self):
        values = [self.engagement_11_completed, self.engagement_12_completed, self.engagement_13_completed, self.engagement_14_completed, self.engagement_15_completed, ]
        return sum(values)

    @property
    def engagement_16_completed(self):
        fields = ['engagement_16']
        return self.completed(fields)

    @property
    def engagement_17_completed(self):
        fields = ['engagement_17']
        return self.completed(fields)

    @property
    def engagement_18_completed(self):
        fields = ['engagement_18']
        return self.completed(fields)

    @property
    def engagement_19_completed(self):
        fields = ['engagement_19']
        return self.completed(fields)

    @property
    def engagement_20_completed(self):
        fields = ['engagement_20']
        return self.completed(fields)

    @property
    def dimension_4_completed(self):
        values = [self.engagement_16_completed, self.engagement_17_completed, self.engagement_18_completed, self.engagement_19_completed, self.engagement_20_completed]
        return sum(values)

    @property
    def dimensions_completed(self):
        values = [self.dimension_1_completed, self.dimension_2_completed, self.dimension_3_completed, self.dimension_4_completed]
        return all(values)


    def completed(self, fields):
        values = [getattr(self, field) != '' and getattr(self, field) is not None for field in fields]
        if all(values):
            return True
        return False

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

    def save(self, *args, **kwargs):
        # update charte_date when a charte is added
        if self.pk is not None:
            orig = Project.objects.get(pk=self.pk)
            if orig.charte != self.charte:
                self.charte_date = date.today()
        else:
            if self.charte:
                self.charte_date = date.today()
        # update label_ecoquartier ("état d'avancement")
        if self.charte_date:
            self.label_ecoquartier = LabelEcoQuartier.objects.get(id=5)
            if self.annee_candidature:
                self.label_ecoquartier = LabelEcoQuartier.objects.get(id=2)
                if self.annee_label:
                    self.label_ecoquartier = LabelEcoQuartier.objects.get(id=3)
        super(Project, self).save(*args, **kwargs)


class ProjectPhoto(models.Model):
    project = models.ForeignKey(Project)
    order = models.PositiveIntegerField()
    title = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', max_length=1500)


class Action(models.Model):
    name = models.CharField("Nom de l'action", max_length=255)
    engagement = models.IntegerField()
    project = models.ForeignKey(Project)
    TODO = '01'
    IN_PROGRESS = '02'
    DONE = '03'
    STATE_CHOICES = (
        (TODO, u'A réaliser'),
        (IN_PROGRESS, u'En cours'),
        (DONE, u'Réalisé'),
    )
    state = models.CharField(u"Etat de l'action",max_length=2, choices=STATE_CHOICES, default=TODO)


class Document(models.Model):
    file = models.FileField("Fichier", upload_to='files/%Y/%m/%d')
    title = models.CharField("Titre", max_length=255)
    project = models.ForeignKey(Project)
    engagement = models.IntegerField()
    TYPE_CHOICES = (
        ('ph', 'Photo'),
        ('pl', 'Plan'),
        ('et', 'Etude, diagnostic'),
        ('pa', 'Planification'),
    )
    type = models.CharField(max_length=2, choices=TYPE_CHOICES, default='fo')


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

