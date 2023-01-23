from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length = 50, null=True)
    last_name = models.CharField(max_length = 50, null=True)
    email_address = models.EmailField(max_length = 150, null=True)
    message = models.TextField(max_length = 1000, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.first_name