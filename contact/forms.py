from django import forms
from django.core.exceptions import ValidationError
from . import models


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Primeiro nome',
            }
        ),
        label='Primeiro Nome',
    )

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Sobrenome',
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
                'required': 'false'
            }
        ),
        label='Descrição'
    )

    class Meta:
        model = models.Contact
        fields = (
            'first_name', 'last_name', 'phone', 'email', 'description', 'category'
        )

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
