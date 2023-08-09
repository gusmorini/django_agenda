from django import forms
from django.core.exceptions import ValidationError
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'somente primeiro nome',
            }
        ),
        label='Nome',
    )

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'sobrenome completo',
            }
        ),
        label='Sobrenome',
    )

    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'telefone',
            }
        ),
        label='Telefone',
        help_text='somente números'
    )

    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'email'
            }
        ),
        label='E-mail'
    )

    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'rows': '10',
            }
        ),
        label='Descrição'
    )

    picture = forms.ImageField(
        widget=forms.FileInput(attrs={'accept': 'image/*'}))

    class Meta:
        model = models.Contact
        fields = ('first_name', 'last_name', 'phone', 'email',
                  'description', 'category', 'picture')

    def clean(self):
        # cleaned_data = self.cleaned_data

        # self.add_error(
        #     'first_name',
        #     ValidationError(
        #         'Mensagem de erro',
        #         code='invalid'
        #     )
        # )
        # self.add_error(
        #     'first_name',
        #     ValidationError(
        #         'Mensagem de erro 2',
        #         code='invalid'
        #     )
        # )

        return super().clean()


class RegisterForm(UserCreationForm):
    ...

    first_name = forms.CharField(required=True, label='Nome')
    last_name = forms.CharField(required=True, label='Sobrenome')
    email = forms.EmailField(label='E-mail')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',
                  'username', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            self.add_error('email', ValidationError(
                'E-mail já existe', code='invalid'))
        return email
