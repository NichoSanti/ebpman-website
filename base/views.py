from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm
from django.http import HttpResponse
from honeypot.decorators import check_honeypot

def home(request):
    context =  {}
    return render(request,'base/home.html', context)

def about(request):
    context = {}
    return render(request, 'base/about.html', context)

@check_honeypot(field_name='hpcontact')
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            subject = 'inquiry'
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email_address': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }
            message = '\n'.join(body.values())
            try:
                send_mail(subject, message, 'ebpman@test.com',
                 ['ebpman@test.com'])
            except BadHeaderError:
                return HttpResponse('invalid header found')
            return redirect('home') 
    form = ContactForm()    
    return render(request, 'base/contact_page.html', {'form':form})






