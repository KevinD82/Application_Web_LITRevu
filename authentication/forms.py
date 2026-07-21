from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from litrevu.models import Ticket, Review


# Formulaire de connexion basique
class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        label="Nom d'utilisateur",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Nom d'utilisateur"}
        ),
    )
    password = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Mot de passe"}
        ),
    )


# Formulaire d'inscription
class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ("username",)


# Formulaire de Ticket (demande de critique)
class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ["title", "description", "image"]
        labels = {
            "title": "Titre du livre / de l'article",
            "description": "Description ou question",
            "image": "Image de couverture",
        }
        widgets = {
            "description": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "De quoi parle ce livre ? Quelle est votre question ?",
                }
            ),
        }


# Formulaire de Critique (Review)
class ReviewForm(forms.ModelForm):
    RATING_CHOICES = [(i, f"- {i}") for i in range(6)]

    rating = forms.ChoiceField(
        choices=RATING_CHOICES, widget=forms.RadioSelect, label="Note"
    )

    class Meta:
        model = Review
        fields = ["headline", "rating", "body"]
        labels = {
            "headline": "Titre de la critique",
            "body": "Commentaire",
        }
        widgets = {
            "body": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "Donnez votre avis détaillé sur l'ouvrage...",
                }
            ),
        }
