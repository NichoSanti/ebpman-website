from django.test import TestCase
from base.forms import ContactForm
class TestContactForm(TestCase):

    def test_is_valid(self):
        form_data = ContactForm(data=
                    {'first_name': 'john', 'last_name': 'smith',
                     'email_address': 'test@gmail.com', 'message':'This is a test'})
        self.assertTrue(form_data.is_valid())

    def test_is_invalid(self):
        form_data = ContactForm(data=
                    {'first_name': 'john', 'last_name': 'smith',
                     'email_address': 123, 'message': 'This is a test'})
        self.assertFalse(form_data.is_valid())

    def test_empty_form(self):
        form = ContactForm()
        self.assertIn("first_name", form.fields)
        self.assertIn("last_name", form.fields)
        self.assertIn("email_address", form.fields)
        self.assertIn("message", form.fields)

    # def test_it_hides_date_field_for_regular_users(self):
    #     contact = ContactForm.objects.create_user(
    #         first_name="funny",
    #         last_name="man",
    #         email_address="just-for-testing@testing.com",
    #         message="dummy-insecure",
    #     )
