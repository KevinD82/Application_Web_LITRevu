from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Modèle représentant un Ticket (demande de critique sur un livre ou un article)
class Ticket(models.Model):
    # Titre du livre ou de l'article (limité à 128 caractères, libellé en français)
    title = models.CharField(max_length=128, verbose_name="Titre")
    # Description optionnelle ou question posée (limitée à 2048 caractères)
    description = models.TextField(
        max_length=2048, blank=True, verbose_name="Description"
    )
    # Relation avec l'utilisateur qui a créé le ticket
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # Image de couverture facultative (enregistrée dans 'tickets_covers/')
    image = models.ImageField(null=True, blank=True, upload_to="tickets_covers/")
    # Date et heure de création enregistrées automatiquement
    time_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Ticket"
        verbose_name_plural = "Tickets"

    # Méthode retournant le titre du ticket pour son affichage textuel
    def __str__(self):
        return self.title


# Modèle représentant une Critique (Review) rédigée en réponse à un ticket
class Review(models.Model):
    # Relation vers le ticket évalué
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE)
    # Note attribuée, contrainte entre 0 et 5 inclus
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        verbose_name="Note",
    )
    # Relation avec l'utilisateur auteur de la critique
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # Titre de la critique
    headline = models.CharField(max_length=128, verbose_name="Titre de la critique")
    # Corps ou texte détaillé de la critique
    body = models.TextField(max_length=2048, blank=True, verbose_name="Commentaire")
    # Date et heure de création de la critique
    time_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Critique"
        verbose_name_plural = "Critiques"

    # Représentation textuelle de la critique
    def __str__(self):
        return f"{self.headline} - {self.rating}/5"


# Modèle de gestion des abonnements entre utilisateurs (système de "follow")
class UserFollows(models.Model):
    # Utilisateur qui effectue l'abonnement
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="following",
    )
    # Utilisateur qui est suivi
    followed_user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="followed_by",
    )

    class Meta:
        # Empêche un utilisateur de suivre deux fois la même personne
        unique_together = ("user", "followed_user")
        # Corrige le nom d'affichage dans le panneau d'administration Django
        verbose_name = "Abonnement"
        verbose_name_plural = "Abonnements"

    def __str__(self):
        return f"{self.user} suit {self.followed_user}"