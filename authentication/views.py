from django.contrib.auth import authenticate, get_user_model, login, logout
from django.shortcuts import redirect, render

from authentication.forms import LoginForm, SignupForm

User = get_user_model()

def login_page(request):
    """Gère la connexion d'un utilisateur."""
    if request.user.is_authenticated:
        return redirect("home")

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
                return redirect("home")
            else:
                message = "Identifiants invalides."

    return render(
        request, "authentication/login.html", context={"form": form, "message": message}
    )


def logout_user(request):
    """Gère la déconnexion de l'utilisateur."""
    logout(request)
    return redirect("login")


def signup_page(request):
    """Gère la création d'un nouveau compte utilisateur."""
    form = SignupForm()
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")

    return render(request, "authentication/signup.html", context={"form": form})