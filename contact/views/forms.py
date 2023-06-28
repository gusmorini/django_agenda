from django.shortcuts import render
from contact.forms import ContactForm


def create(request):
    context = {
        'form': ContactForm()
    }

    if request.method == 'POST':
        context = {
            'form': ContactForm(request.POST)
        }

    return render(
        request,
        'contact/create.html',
        context
    )
