# class Contact(models.Model):
#     first_name = models.CharField(max_length = 50, null=True)
#     last_name = models.CharField(max_length = 50, null=True)
#     email_address = models.EmailField(max_length = 150, null=True)
#     message = models.TextField(max_length = 1000, null=True)
#     created = models.DateTimeField(auto_now_add=True, null=True)

#     def __str__(self):
#         return self.email_address


from base.models import Contact   
from django.test import TestCase
class ContactModelTest(TestCase): 

    @classmethod
    def setUpTestData(cls): 
        Contact.objects.create(first_name='John', last_name='Bob')
    
    def test_email_address_length(self):
        contact = Contact.objects.get(id=1)
        max_length = Contact._meta.get_field('email_address').max_length
        self.assertEqual(max_length, 150)
         

