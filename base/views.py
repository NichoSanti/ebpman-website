from django.shortcuts import render, redirect
from .forms import ContactForm
from django.http import HttpResponseRedirect

def home(request):
    context =  {}
    return render(request,'base/home.html', context)

def about(request):
    context = {}
    return render(request, 'base/about.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            form.send_mail()
            return HttpResponseRedirect('home')
    else:
        form = ContactForm()
    
    return render(request, 'base/contact_page.html', {'form':form})






