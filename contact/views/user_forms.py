from django.shortcuts import render, redirect
from contact.forms import RegisterForm
from django.urls import reverse
from django.contrib import messages, auth
from django.contrib.auth.forms import AuthenticationForm


def register(request):

    form = RegisterForm()
    form_action = reverse('contact:register')

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():
            contact = form.save()
            messages.success(request, 'Usuário registrado')
            return redirect('contact:index')

    return render(
        request,
        'contact/register.html',
        {
            'form': form,
            'form_action': form_action
        }
    )


def login_view(request):

    form = AuthenticationForm(request)
    form_action = reverse('contact:login')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect('contact:login')

    return render(
        request,
        'contact/login.html',
        {
            'form': form,
            'form_action': form_action
        }
    )


def logout(request):
    auth.logout(request)
    return redirect('contact:login')
