from django import forms

from games.models import List


class AuthorListEditForm(forms.ModelForm):
    class Meta:
        model = List
        fields = [
            'title',
            'description',
        ]

        labels = {
           'title': 'Nome da Lista',
           'description': 'Descrição',
           'games': ''
        }
        error_messages = {
            'title': {
                'required': 'Esse campo não pode ficar vazio.',
            },   
            'description': {
                'required': 'Esse campo não pode ficar vazio.',
            }, 
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'editInput',
                'id': 'title',
                'autocomplete': 'off',
                'required': 'true',
                'placeholder': 'Nome da Lista',
            }),
            'description': forms.Textarea(attrs={
                'class': 'editInput',
                'id': 'description',
                'autocomplete': 'off',
                'required': 'true',
                'placeholder': 'Digite aqui a descrição da lista...'
            }),
        }