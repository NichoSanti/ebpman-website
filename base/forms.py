from django import forms
from .models import Contact
from django.core.mail import send_mail
from django.conf import settings

class ContactForm(forms.ModelForm):
    honeypot = forms.CharField(required=False, widget=forms.HiddenInput(), label="Leave empty")
    class Meta:
        model = Contact
        fields = [
            'first_name',
            'last_name',
            'email_address',
            'message',
            'honeypot',
        ]

    def clean_honeypot(self):
        honeypot = self.cleaned_data['honeypot']
        if len(honeypot):
            raise forms.ValidationError(
                self.fields['honeypot'].label,
            )
        return honeypot

    def send_mail(self):
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        email = self.cleaned_data['email_address']
        message = self.cleaned_data['message']
        message = 'Message from {first_name} {last_name} <{email}>:\n\n{message}'.format(
            first_name=first_name,
            last_name=last_name,
            email=email,
            message=message,
        )
        send_mail(
            'Subject here',
            message,
            settings.DEFAULT_FROM_EMAIL,
            ['Ebpman@test.com'],
            fail_silently=False,
        )

    