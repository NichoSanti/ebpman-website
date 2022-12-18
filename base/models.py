from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length = 50, default='test first name')
    last_name = models.CharField(max_length = 50, default='test last name')
    email_address = models.EmailField(max_length = 150, default='test email')
    message = models.CharField(max_length = 1000, default='test message')

    def __str__(self):
        return self.email