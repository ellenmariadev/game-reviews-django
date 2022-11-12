from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        label='Usuário',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'floatingInput',
            'autocomplete': 'off',
            'placeholder': 'Usuário',
        }),
    )

    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'id': 'floatingInput',
            'autocomplete': 'off',
            'placeholder': 'Senha'
        }),
    )