from django.shortcuts import render, redirect, get_object_or_404
from contact.forms import ContactForm
from contact.models import Contact
from django.urls import reverse


def create(request):
    form_action = reverse('contact:create')

    context = {
        'form': ContactForm(),
        'form_action': form_action
    }

    if request.method == 'POST':

        form = ContactForm(request.POST, request.FILES)
        context['form'] = form

        if form.is_valid():
            contact = form.save()
            return redirect('contact:index')

    return render(request, 'contact/create.html', context)


def update(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id, show=True)

    form_action = reverse('contact:update', args=(contact_id,))

    context = {
        'form': ContactForm(instance=contact),
        'form_action': form_action
    }

    if request.method == 'POST':

        form = ContactForm(request.POST, request.FILES, instance=contact)
        context['form'] = form

        if form.is_valid():
            c = form.save()
            return redirect('contact:contact', contact_id=c.pk)

    return render(request, 'contact/create.html', context)


def delete(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id, show=True)
    confirm = request.POST.get('confirm', 'no')

    if confirm == 'yes':
        contact.delete()
        return redirect('contact:index')

    context = {'contact': contact, 'confirm': confirm}

    return render(request, 'contact/contact.html', context)
