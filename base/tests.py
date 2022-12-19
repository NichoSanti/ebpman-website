from django.test import TestCase
from .forms import ContactForm

class ContactFormTest(TestCase):
    def setUp(self):
        form_data = {
            'first_name': 'John', 
            'last_name': 'Smith', 
            'email_address': 'johnsmith@gmail.com',
            'message': 'This is a test message',
            } 
        form = ContactForm(data=form_data)
        self.assertTrue(form.is_valid())
    
      

