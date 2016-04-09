from django.test import TestCase
from eventex.subscriptions.models import Subscription


class SubscriptionDetailGet(TestCase):
    def setUp(self):
        self.obj = Subscription.objects.create(
                name='Xelo Ximira',
                cpf='12345678910',
                email='xelo@xelo.com',
                phone='1122334455'
        )
        self.resp = self.client.get('/inscricao/{}/'.format(self.obj.pk))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(
                self.resp,
                'subscriptions/subscription_detail.html'
        )

    def test_context(self):
        subscription = self.resp.context['subscription']
        self.assertIsInstance(subscription, Subscription)

    def test_html(self):
        contents = (
                self.obj.name,
                self.obj.cpf,
                self.obj.email,
                self.obj.phone
        )
        with self.subTest():
            for content in contents:
                self.assertContains(self.resp, content)


class SubscriptionDetailNotFound(TestCase):

    def setUp(self):
        self.resp = self.client.get('/inscricao/0/')

    def test_not_found(self):
        self.assertEqual(404, self.resp.status_code)
