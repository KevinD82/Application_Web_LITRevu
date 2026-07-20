from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    """Page d'accueil (flux) accessible uniquement si connecté."""
    return render(request, "litrevu/home.html")
