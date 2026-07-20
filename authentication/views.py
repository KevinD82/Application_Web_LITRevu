from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import LoginForm, SignupForm


# login_page : Affiche le formulaire de connexion. Si l'utilisateur valide le formulaire (POST), Django vérifie son identifiant et son mot de passe avec authenticate().
# S'ils sont bons, il ouvre la session avec login()
def login_page(request):
    """Gère la connexion d'un utilisateur."""
    form = LoginForm()
    message = ""

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                return redirect("home")  # On redirigera vers la page d'accueil (flux)
            else:
                message = "Identifiants invalides."

    return render(
        request, "authentication/login.html", context={"form": form, "message": message}
    )


# logout_user : Ferme la session avec logout() et redirige vers la page de connexion.
def logout_user(request):
    """Gère la déconnexion de l'utilisateur."""
    logout(request)
    return redirect("login")


# signup_page : Crée le nouveau compte en BDD via form.save(), puis connecte automatiquement le nouvel utilisateur.
def signup_page(request):
    """Gère la création d'un nouveau compte utilisateur."""
    form = SignupForm()
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(
                request, user
            )  # Connecte directement l'utilisateur après l'inscription
            return redirect("home")

    return render(request, "authentication/signup.html", context={"form": form})
