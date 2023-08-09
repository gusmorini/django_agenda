from django.shortcuts import render, redirect
from contact.forms import RegisterForm
from django.urls import reverse


def register(request):

    form = RegisterForm()
    form_action = reverse('contact:register')

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():
            contact = form.save()
            return redirect('contact:register')

    return render(
        request,
        'contact/register.html',
        {
            'form': form,
            'form_action': form_action
        }
    )
