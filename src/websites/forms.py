from django import forms

from.models import Website


class WebsiteForm(forms.ModelForm):
    url = forms.URLField(max_length=200, initial='https://')

    class Meta:
        model = Website
        fields = "__all__"
