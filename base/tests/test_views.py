from django.test import TestCase
from base.forms import ContactForm 
from django.urls import reverse

class ContactViewTestCase(TestCase):

    def test_contact_view_success(self):
        data = {
            'first_name': 'Jane',
            'last_name': 'Doe',
            'email_address': 'janedoe@test.com',
            'message': 'This is a test message'
        }
        form = ContactForm(data=data)
        self.assertTrue(form.is_valid())

        response = self.client.post(reverse('contact-page'), data)

        self.assertEqual(response.status_code, 302)
        
    def test_contact_view_invalid(self):
        data = {
            'first_name': '',
            'last_name': '',
            'email_address': '',
            'message': ''
        }
        form = ContactForm(data=data)
        self.assertFalse(form.is_valid())

class HomeViewTestCase(TestCase):
    def setUp(self):
        self.url = reverse('home')

    def test_home_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/home.html')
