from dal import autocomplete

from .models import Commune


class CommuneAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Commune.objects.all().order_by('label')
        if self.q:
            qs = qs.filter(label__istartswith=self.q)
        return qs