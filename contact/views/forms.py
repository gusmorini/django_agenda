from django.shortcuts import render, redirect
from contact.forms import ContactForm


def create(request):
    context = {
        'form': ContactForm()
    }

    if request.method == 'POST':

        form = ContactForm(request.POST)

        context = {
            'form': form
        }

        if form.is_valid():
            contact = form.save()
            return redirect('contact:contact', contact_id=contact.pk)

    return render(
        request,
        'contact/create.html',
        context
    )
