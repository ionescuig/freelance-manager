from django import forms

from .models import Subscription


class SubscriptionForm(forms.ModelForm):
    date_created = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    date_renewal = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Subscription
        fields = '__all__'
        widgets = {
            'notes': forms.Textarea(attrs={'rows': 8}),
        }

    def __init__(self, *args, **kwargs):
        super(SubscriptionForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control form-control-sm'


class SubscriptionUpdateForm(forms.ModelForm):
    date_created = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    date_renewal = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Subscription
        fields = ['date_created', 'date_renewal', 'notify_by_email', 'notes']
        widgets = {
            'notes': forms.Textarea(attrs={'rows': 8}),
        }

    def __init__(self, *args, **kwargs):
        super(SubscriptionUpdateForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control form-control-sm'
