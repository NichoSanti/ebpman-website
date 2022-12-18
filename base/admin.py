from django.contrib import admin
from .models import Contact
from .forms import ContactForm

admin.site.register(Contact)

