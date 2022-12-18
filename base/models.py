from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length = 50, label='Your name')
    last_name = models.CharField(max_length = 50, label='Your last name')
    email_address = models.EmailField(max_length = 150, label='Your email adress')
    message = models.CharField(max_length = 1000)

    def __str__(self):
        return self.email