from django.test import TestCase
from base.forms import ContactForm
class TestContactForm(TestCase):

    def test_empty_form(self):
        form = ContactForm()
        self.assertIn("first_name", form.fields)
        self.assertIn("last_name", form.fields)
        self.assertIn("email_address", form.fields)
        self.assertIn("message", form.fields)

    