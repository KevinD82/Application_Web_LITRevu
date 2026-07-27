from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Décorateur exigeant que l'utilisateur soit connecté pour accéder à cette vue
@login_required
def home(request):
    """Page d'accueil (flux) accessible uniquement si connecté."""
    # Rendu du template HTML de la page d'accueil (flux) pour l'utilisateur authentifié
    return render(request, "litrevu/home.html")