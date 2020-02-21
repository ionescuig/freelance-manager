from django import forms

from.models import Website


class WebsiteForm(forms.ModelForm):
    url = forms.URLField(max_length=200, initial='https://')

    class Meta:
        model = Website
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(WebsiteForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control form-control-sm'
