from django import forms
from django.core.exceptions import ValidationError
from eventex.subscriptions.models import Subscription
from eventex.subscriptions.validators import validate_cpf


class SubscriptionFormOld(forms.Form):
    """Not used"""
    name = forms.CharField(label='Nome')
    cpf = forms.CharField(label='CPF', validators=[validate_cpf])
    email = forms.EmailField(label='Email', required=False)
    phone = forms.CharField(label='Telefone', required=False)

    def clean_name(self):
        name = self.cleaned_data['name']
        words = [w.capitalize() for w in name.split()]
        return ' '.join(words)

    def clean(self):
        get_email = self.cleaned_data.get('email')
        get_phone = self.cleaned_data.get('phone')
        if not get_email and not get_phone:
            raise ValidationError('Informe o seu email ou telefone')

        return self.cleaned_data


class SubscriptionForm(forms.ModelForm):

    class Meta:
        model = Subscription
        fields = ['name', 'cpf', 'email', 'phone']

    def clean_name(self):
        name = self.cleaned_data['name']
        words = [w.capitalize() for w in name.split()]
        return ' '.join(words)

    def clean(self):
        self.cleaned_data = super().clean()
        get_email = self.cleaned_data.get('email')
        get_phone = self.cleaned_data.get('phone')
        if not get_email and not get_phone:
            raise ValidationError('Informe o seu email ou telefone')

        return self.cleaned_data
