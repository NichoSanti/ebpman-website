from xml.dom.minidom import ReadOnlySequentialNamedNodeMap
from django import forms
from .models import Contact

# class ContactForm(forms.Form):
#     first_name = forms.CharField(max_length = 50, label='Your name')
#     last_name = forms.CharField(max_length = 50, label='Your last name')
#     email_address = forms.EmailField(max_length = 150, label='Your email adress')
#     message = forms.CharField(max_length = 1000)

def ContactForm(ModelForm):
    class Meta:
        model = Contact
        field = '__all__'
        

