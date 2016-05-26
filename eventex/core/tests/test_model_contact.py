from django.core.exceptions import ValidationError
from django.test import TestCase
from eventex.core.models import Speaker, Contact


class ContactModelTest(TestCase):

    def setUp(self):
        self.speaker = Speaker.objects.create(
            name='Ronald Theodoro',
            slug='ronald-theodoro',
            photo='http://migre.me/tUsq9',
        )

    def test_email(self):
        Contact.objects.create(
            speaker=self.speaker,
            kind=Contact.EMAIL,
            value='ronald@ronald.com'
        )

        self.assertTrue(Contact.objects.exists())

    def test_phone(self):
        Contact.objects.create(
            speaker=self.speaker,
            kind=Contact.PHONE,
            value='11-58585858'
        )

        self.assertTrue(Contact.objects.exists())

    def test_choices(self):
        """Contact kind should be limited to E or P"""
        contact = Contact(speaker=self.speaker, kind='A', value='B')
        self.assertRaises(ValidationError, contact.full_clean)

    def test_str(self):
        contact = Contact(
            speaker=self.speaker,
            kind='E',
            value='ronald@ronald.com'
        )
        self.assertEqual('ronald@ronald.com', str(contact))


class ContactManagerTest(TestCase):

    def setUp(self):
        s = Speaker.objects.create(
            name='Xelo Ximira',
            slug='xelo-ximira',
            photo='https://i.ytimg.com/vi/tIzf_MAbxyg/maxresdefault.jpg',
        )
        s.contact_set.create(kind=Contact.EMAIL, value='xelo@ximira.com')
        s.contact_set.create(kind=Contact.PHONE, value='11958585858')

    def test_emails(self):
        qs = Contact.objects.emails()
        expected = ['xelo@ximira.com']
        self.assertQuerysetEqual(qs, expected, lambda o: o.value)

    def test_phone(self):
        qs = Contact.objects.phones()
        expected = ['11958585858']
        self.assertQuerysetEqual(qs, expected, lambda o: o.value)
