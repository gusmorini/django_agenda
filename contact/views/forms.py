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
            form.save()
            return redirect('contact:index')

    return render(
        request,
        'contact/create.html',
        context
    )
