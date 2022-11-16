from django import forms

from games.models import ReviewRating


class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewRating
        fields = ['review', 'rating']

        widgets = {
            'review': forms.Textarea(attrs={
                'class': 'review-game',
                'required': 'true',
                'placeholder': 'Escreva aqui...',
            })
        }