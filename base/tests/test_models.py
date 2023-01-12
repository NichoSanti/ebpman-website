


from base.models import Contact   
from django.test import TestCase
class ContactModelTest_length(TestCase): 

    @classmethod
    def setUpTestData(cls): 
        Contact.objects.create(first_name='John', last_name='Bob')
    
    def test_email_address_length(self):
        contact = Contact.objects.get(id=1)
        max_length = contact._meta.get_field('email_address').max_length
        self.assertEqual(max_length, 150)
    
    def test_first_name_length(self):
        contact = Contact.objects.get(id=1)
        max_length = contact._meta.get_field('first_name').max_length
        self.assertEqual(max_length, 50)

    def test_last_name_length(self):
        contact = Contact.objects.get(id=1)
        max_length = contact._meta.get_field('last_name').max_length
        self.assertEqual(max_length, 50)

    def test_message_length(self):
        contact = Contact.objects.get(id=1)
        max_length = contact._meta.get_field("message").max_length
        self.assertEqual(max_length, 1000)







