from xml.dom.minidom import ReadOnlySequentialNamedNodeMap
from django import forms

class ContactForm(forms.Form):
    first_name = forms.CharField(max_length = 50, label='Name')
    last_name = forms.CharField(max_length = 50, label='Last Name')
    email_address = forms.EmailField(max_length = 150, label='Email')
    message = forms.CharField(max_length = 1000)

