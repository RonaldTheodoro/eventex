from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscriptionFormTest(TestCase):
    def test_has_form_fields(self):
        """Form must have 4 fields"""
        fields = ['name', 'cpf', 'email', 'phone']
        form = SubscriptionForm()
        self.assertSequenceEqual(fields, list(form.fields))

    def test_cpf_is_digit(self):
        """CPF must only accept digits"""
        form = self.make_validate_form(cpf='0123456789A')
        self.assertFormErrorCode(form, 'cpf', 'digits')

    def test_cpf_has_11_digit(self):
        """CPF must have 11 digits"""
        form = self.make_validate_form(cpf='1234')
        self.assertFormErrorCode(form, 'cpf', 'length')

    def make_validate_form(self, **kwargs):
        valid = dict(
            name='Xelo Ximira',
            cpf='12345678910',
            email='xelo@xelo.com',
            phone='1123345455'
        )
        data = dict(valid, **kwargs)
        form = SubscriptionForm(data)
        form.is_valid()
        return form

    def assertFormErrorCode(self, form, field, code):
        errors = form.errors.as_data()
        errors_list = errors[field]
        exception = errors_list[0]
        self.assertEqual(code, exception.code)
