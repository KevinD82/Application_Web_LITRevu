from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Modèle représentant un Ticket (demande de critique sur un livre ou un article)
class Ticket(models.Model):
    # Titre du livre ou de l'article (limité à 128 caractères, libellé en français)
    title = models.CharField(max_length=128, verbose_name="Titre")
    # Description optionnelle ou question posée (limitée à 2048 caractères, champ optionnel avec blank=True)
    description = models.TextField(
        max_length=2048, blank=True, verbose_name="Description"
    )
    # Relation avec l'utilisateur qui a créé le ticket (suppression en cascade si l'utilisateur est supprimé)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # Image de couverture facultative (enregistrée dans le dossier 'tickets_covers/')
    image = models.ImageField(null=True, blank=True, upload_to="tickets_covers/")
    # Date et heure de création enregistrées automatiquement à l'insertion
    time_created = models.DateTimeField(auto_now_add=True)

    # Méthode magique retournant le titre du ticket pour son affichage textuel (ex: dans l'admin)
    def __str__(self):
        return self.title


# Modèle représentant une Critique (Review) rédigée en réponse à un ticket
class Review(models.Model):
    # Relation vers le ticket évalué (suppression en cascade si le ticket est supprimé)
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE)
    # Note attribuée, contrainte par des validateurs entre 0 et 5 inclus
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        verbose_name="Note",
    )
    # Relation avec l'utilisateur auteur de la critique
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # Titre de la critique (limité à 128 caractères)
    headline = models.CharField(max_length=128, verbose_name="Titre de la critique")
    # Corps ou texte détaillé de la critique (optionnel, limité à 2048 caractères)
    body = models.TextField(max_length=2048, blank=True, verbose_name="Commentaire")
    # Date et heure de création de la critique enregistrées automatiquement
    time_created = models.DateTimeField(auto_now_add=True)

    # Représentation textuelle de la critique combinant son titre et sa note sur 5
    def __str__(self):
        return f"{self.headline} - {self.rating}/5"


# Modèle de gestion des abonnements entre utilisateurs (système de "follow")
class UserFollows(models.Model):
    # Utilisateur qui effectue l'abonnement (accès inversé via la relation 'following')
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="following",
    )
    # Utilisateur qui est suivi (accès inversé via la relation 'followed_by')
    followed_user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="followed_by",
    )

    class Meta:
        # Contrainte d'unicité : empêche un utilisateur de suivre deux fois la même personne
        unique_together = ("user", "followed_user")