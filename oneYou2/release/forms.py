from django import forms
from django.forms import ModelForm

from pages.models import OneYou2Page


class ReleaseAdminForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ReleaseAdminForm, self).__init__(*args, **kwargs)
        pages_for_selector = []
        pages = OneYou2Page.objects.all()
        initial_selection = []
        if self.instance:
            for relation in self.instance.revisions.all():
                initial_selection.append(str(relation.revision.page.id))
        for page in pages:
            pages_for_selector.append((str(page.id), page.title))
        self.fields['page_name'] = forms.MultipleChoiceField(choices=pages_for_selector, required=False,
                                                             initial=initial_selection)

    def clean(self):
        cleaned_data = super(ReleaseAdminForm, self).clean()
        return cleaned_data
