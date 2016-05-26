from django.test import TestCase
from django.core import mail
from django.shortcuts import resolve_url as r


class SubscribePostValid(TestCase):

    def setUp(self):
        data = dict(
            name='Xelo Ximira',
            cpf='12345678910',
            email='xelo@xelo.com',
            phone='1122334455'
        )
        self.client.post(r('subscriptions:new'), data)
        self.email = mail.outbox[0]

    def test_subscribe_email_subject(self):
        self.assertEqual('Confirmação de inscrição', self.email.subject)

    def test_subscribe_email_from(self):
        self.assertEqual('hanschucrteslabrat@gmail.com', self.email.from_email)

    def test_subscribe_email_to(self):
        to = ['hanschucrteslabrat@gmail.com', 'xelo@xelo.com']
        self.assertEqual(to, self.email.to)

    def test_subscribe_email_body(self):
        conts = ('Xelo Ximira', '12345678910', 'xelo@xelo.com', '1122334455')
        for cont in conts:
            with self.subTest():
                self.assertIn(cont, self.email.body)
