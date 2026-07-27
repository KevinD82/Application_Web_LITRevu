from typing import ClassVar

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from litrevu.models import Review, Ticket


# Formulaire de connexion basique
class LoginForm(forms.Form):
    # Champ pour le nom d'utilisateur avec une limite de 150 caractères et des attributs CSS Bootstrap
    username = forms.CharField(
        max_length=150,
        label="Nom d'utilisateur",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Nom d'utilisateur"}
        ),
    )
    # Champ pour le mot de passe masqué (PasswordInput)
    password = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Mot de passe"}
        ),
    )


# Formulaire d'inscription (personnalisé en français)
class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # Utilisation du modèle utilisateur personnalisé défini dans les paramètres Django
        model = get_user_model()
        fields = ("username",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Modification des libellés (Labels) en français
        self.fields["username"].label = "Nom d'utilisateur"
        self.fields["password1"].label = "Mot de passe"
        self.fields["password2"].label = "Confirmation du mot de passe"

        # Modification des textes d'aide pour guider l'utilisateur
        self.fields["username"].help_text = "Requis. 150 caractères maximum."
        self.fields["password1"].help_text = (
            "Votre mot de passe doit contenir au moins 8 caractères, "
            "incluant au moins 1 majuscule et 1 caractère spécial."
        )
        self.fields[
            "password2"
        ].help_text = "Saisissez le même mot de passe que précédemment."


# Formulaire de Ticket (demande de critique)
class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ("title", "description", "image")

        # Ajout de l'annotation ClassVar[dict] pour satisfaire l'analyseur de code Ruff
        labels: ClassVar[dict] = {
            "title": "Titre du livre / de l'article",
            "description": "Description ou question",
            "image": "Image de couverture",
        }
        widgets: ClassVar[dict] = {
            # Transformation de la description en zone de texte (Textarea) avec lignes et placeholder
            "description": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": (
                        "De quoi parle ce livre ? Quelle est votre question ?"
                    ),
                }
            ),
        }


# Formulaire de Critique (Review)
class ReviewForm(forms.ModelForm):
    # Génération des choix de notes de 0 à 5 sous forme de tuple
    RATING_CHOICES = tuple((i, f"- {i}") for i in range(6))

    # Champ de notation affiché sous forme de boutons radios
    rating = forms.ChoiceField(
        choices=RATING_CHOICES, widget=forms.RadioSelect, label="Note"
    )

    class Meta:
        model = Review
        fields = ("headline", "rating", "body")

        # Ajout de l'annotation ClassVar[dict] pour satisfaire l'analyseur de code Ruff
        labels: ClassVar[dict] = {
            "headline": "Titre de la critique",
            "body": "Commentaire",
        }
        widgets: ClassVar[dict] = {
            # Transformation du corps de la critique en zone de texte (Textarea)
            "body": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "Donnez votre avis détaillé sur l'ouvrage...",
                }
            ),
        }