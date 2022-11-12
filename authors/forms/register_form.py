import re

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class RegisterForm(forms.ModelForm):

    def strong_password(password):
        regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$')

        if not regex.match(password):
            raise ValidationError((
                'Senha deve conter pelo menos uma letra maiúscula, uma letra minúscula e um número. Tem que ter pelo menos 8 caracteres.'
            ),
                code='Invalid'
            )

    # email = forms.EmailField(
    #     error_messages={'required': 'Esse campo não pode ficar vazio.', 
    #     'invalid': 'Digite um e-mail válido.'},
    #     required=True,
    #     label='E-mail',
    # )


    username = forms.CharField(
        label='Usuário',
        # help_text=(
        #     'Username must have letters, numbers or one of those @.+-_. '
        #     'The length should be between 4 and 150 characters.'
        # ),
        error_messages={
            'required': 'Esse campo não pode ficar vazio.',
            'min_length': 'Usuário deve ter pelo menos 4 caracteres.',
            'max_length': 'Usuário deve ter menos de 25 caracteres.',
            'unique': 'Esse nome de usuário já existe.'
        },
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'floatingInput',
            'autocomplete': 'off',
            'required': 'true',
            'placeholder': 'Usuário',
        }),
        min_length=3, max_length=25,
    )

    password = forms.CharField(
        error_messages={'required': 'Esse campo não pode ficar vazio.'},
        required=True,
        label='Senha',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'id': 'floatingInput',
            'autocomplete': 'off',
            'required': 'true',
            'placeholder': 'Confirmar Senha'
        }),
        validators=[strong_password]
    )

    password2 = forms.CharField(
        required=True,
        label='Confirmar Senha',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'id': 'floatingInput',
            'autocomplete': 'off',
            'required': 'true',
            'placeholder': 'Confirmar Senha'
        })
    )

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
        ]
        labels = {
           'username': 'Usuário',
           'email': 'E-mail',
           'password': 'Senha',
           'password2': 'Confirmar Senha'
        }
        error_messages = {
            'username': {
                'required': 'Esse campo não pode ficar vazio.',
                'invalid': 'Digite um nome de usuário válido.'
            },   
            'email': {
                'required': 'Esse campo não pode ficar vazio.',
                'invalid': 'Digite um e-mail válido.'
            },
            'senha': {
                'required': 'Esse campo não pode ficar vazio.'
            },   
        }
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'floatingInput',
                'autocomplete': 'off',
                'required': 'true',
                'placeholder': 'Usuário',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'id': 'floatingInput',
                'autocomplete': 'off',
                'required': 'true',
                'placeholder': 'E-mail'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'id': 'floatingInput',
                'autocomplete': 'off',
                'required': 'true',
                'placeholder': 'Senha',
            }),
        }

    def clean_password(self):
        data = self.cleaned_data.get("password")

        if 'oi' in data: 
            raise ValidationError(
                "Não digite %(value)s na senha",
                code='invalid',
                params={'value': '"oi"'}
            )
        return data

    def clean_email(self):
        email = self.cleaned_data.get('email', '')
        exists = User.objects.filter(email=email).exists()

        if exists:
            raise ValidationError(
                'Esse e-mail já está registrado.', code='invalid',
            )

        return email

    
    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password != password2:
            password_confirmation_error = ValidationError(
                'As senhas estão diferentes.',
                code='invalid'
            )
            raise ValidationError({
                'password2': password_confirmation_error,
                # 'password2': [
                #     password_confirmation_error,
                # ],
            })