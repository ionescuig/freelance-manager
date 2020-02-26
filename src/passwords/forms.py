from django import forms

from.models import Password


class PasswordForm(forms.ModelForm):
    class Meta:
        model = Password
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(PasswordForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control form-control-sm'
