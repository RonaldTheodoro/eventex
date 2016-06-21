from datetime import datetime
from django.test import TestCase
from django.shortcuts import resolve_url as r
from eventex.subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):

    def setUp(self):
        self.obj = Subscription(
            name='Xelo Ximira',
            cpf='12345678910',
            email='xelo@xelo.com',
            phone='1122334455'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """Subscription must have an auto created_at attr."""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Xelo Ximira', str(self.obj))

    def test_paid_default_to_false(self):
        """By default paid must be False."""
        self.assertEqual(False, self.obj.paid)

    def test_get_absolute_url(self):
        url = r('subscriptions:detail', self.obj.pk)
        self.assertEqual(url, self.obj.get_absolute_url())
