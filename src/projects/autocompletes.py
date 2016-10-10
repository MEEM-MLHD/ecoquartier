from django.contrib.auth.models import User

from dal import autocomplete

from .models import Commune


class CommuneAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Commune.objects.all().order_by('label')
        if self.q:
            qs = qs.filter(label__istartswith=self.q)
        return qs


class EditorAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = User.objects.all().order_by('username')  #.exclude(user=self.request.user)
        if self.q:
            qs = qs.filter(username__icontains=self.q)
        return qs