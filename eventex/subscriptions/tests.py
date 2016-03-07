from django.core import mail
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscribeTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/inscricao/')
        self.form = self.resp.context['form']

    def test_get(self):
        """GET /inscricao/ must return status code 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """Must use subscriptions/subscription_form.html"""
        self.assertTemplateUsed(
                self.resp,
                'subscriptions/subscription_form.html'
        )

    def test_html(self):
        """Html must contain input tags"""
        self.assertContains(self.resp, '<form')
        self.assertContains(self.resp, '<input', 6)
        self.assertContains(self.resp, 'type="text"', 3)
        self.assertContains(self.resp, 'type="email"')
        self.assertContains(self.resp, 'type="submit"')

    def test_csrf(self):
        """Html must contain csrf"""
        self.assertContains(self.resp, "csrfmiddlewaretoken")

    def test_has_form(self):
        """Context must have subscription form"""
        self.assertIsInstance(self.form, SubscriptionForm)

    def test_has_form_fields(self):
        """Form must have 4 fields"""
        self.assertSequenceEqual(
                ['name', 'cpf', 'email', 'phone'],
                list(self.form.fields)
        )


class SubscribePostTest(TestCase):
    def setUp(self):
        data = dict(
                name='Xelo Ximira',
                cpf='12345678910',
                email='xelo@xelo.com',
                phone='1122334455'
        )
        self.response = self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_post(self):
        """Valid POST should redirect to /inscricao/"""
        self.assertEqual(302, self.response.status_code)

    def test_send_subscribe_email(self):
        self.assertEqual(1, len(mail.outbox))

    def test_subscribe_email_subject(self):
        self.assertEqual('Confirmação de inscrição', self.email.subject)

    def test_subscribe_email_from(self):
        self.assertEqual('contato@eventex.com.br', self.email.from_email)

    def test_subscribe_email_to(self):
        self.assertEqual(
                ['contato@eventex.com.br', 'xelo@xelo.com'],
                self.email.to
        )

    def test_subscribe_email_body(self):
        self.assertIn('Xelo Ximira', self.email.body)
        self.assertIn('12345678910', self.email.body)
        self.assertIn('xelo@xelo.com', self.email.body)
        self.assertIn('1122334455', self.email.body)
