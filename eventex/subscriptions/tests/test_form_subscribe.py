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

    def test_name_must_be_capitalized(self):
        """Name must be capitalize"""
        # RONALD theodoro -> Ronald Theodoro
        form = self.make_validate_form(name='RONALD theodoro')
        self.assertEqual('Ronald Theodoro', form.cleaned_data['name'])

    def test_email_is_optional(self):
        """Email is optional"""
        form = self.make_validate_form(email='')
        self.assertFalse(form.errors)

    def test_phone_is_optional(self):
        """Phone is optional"""
        form = self.make_validate_form(phone='')
        self.assertFalse(form.errors)

    def test_must_inform_email_or_phone(self):
        """Email and Phone ar optional, but one must be informed"""
        form = self.make_validate_form(email='', phone='')
        self.assertListEqual(['__all__'], list(form.errors))

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
