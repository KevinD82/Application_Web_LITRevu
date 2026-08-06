# Importation des fonctions utilitaires pour gérer l'authentification native de Django
from django.contrib.auth import authenticate, get_user_model, login, logout

# Importation des raccourcis Django pour rediriger l'utilisateur ou afficher un template HTML
from django.shortcuts import redirect, render

# Importation des formulaires personnalisés d'inscription et de connexion situés dans l'app authentication
from authentication.forms import LoginForm, SignupForm

# Récupération dynamique du modèle utilisateur actif (recommandé dans Django)
User = get_user_model()

def login_page(request):
    """Gère la connexion d'un utilisateur."""
    
    # 1. Si l'utilisateur est déjà connecté, on le redirige directement vers la page d'accueil
    if request.user.is_authenticated:
        return redirect("home")

    # 2. Initialisation d'un formulaire de connexion vide et d'une variable de message d'erreur vide
    form = LoginForm()
    message = ""

    # 3. Vérification si le formulaire a été soumis (méthode HTTP POST)
    if request.method == "POST":
        form = LoginForm(request.POST)
        
        # Validation des données saisies selon les règles du formulaire
        if form.is_valid():
            # Tentative d'authentification avec le nom d'utilisateur et le mot de passe nettoyés
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            
            # Si l'utilisateur existe et que le mot de passe est correct
            if user is not None:
                # Connexion effective de l'utilisateur (création de la session)
                login(request, user)
                # Redirection vers la page d'accueil
                return redirect("home")
            else:
                # Sinon, préparation d'un message d'erreur en cas d'identifiants incorrects
                message = "Identifiants invalides."

    # 4. Affichage de la page de connexion (template HTML) en y injectant le formulaire et le message éventuel
    return render(
        request, "authentication/login.html", context={"form": form, "message": message}
    )


def logout_user(request):
    """Gère la déconnexion de l'utilisateur."""
    
    # Suppression de la session en cours de l'utilisateur
    logout(request)
    
    # Redirection vers la page de connexion
    return redirect("login")


def signup_page(request):
    """Gère la création d'un nouveau compte utilisateur."""
    
    # Initialisation d'un formulaire d'inscription vide
    form = SignupForm()
    
    # Si le formulaire d'inscription est soumis
    if request.method == "POST":
        form = SignupForm(request.POST)
        
        # Vérification de la validité des données
        if form.is_valid():
            # Enregistrement du nouvel utilisateur dans la base de données
            user = form.save()
            
            # Connexion automatique du nouvel utilisateur fraîchement inscrit
            login(request, user)
            
            # Redirection vers la page d'accueil
            return redirect("home")

    # Affichage du formulaire d'inscription dans le template HTML dédié
    return render(request, "authentication/signup.html", context={"form": form})