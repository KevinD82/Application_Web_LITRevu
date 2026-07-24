from itertools import chain

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import CharField, Value
from django.shortcuts import redirect, render

from litrevu.models import Review, Ticket

from .forms import LoginForm, ReviewForm, SignupForm, TicketForm


# login_page : Affiche le formulaire de connexion.
def login_page(request):
    """Gère la connexion d'un utilisateur."""
    # Si l'utilisateur est déjà connecté, on le redirige directement sur le flux !
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


# logout_user : Ferme la session avec logout() et redirige vers la page de connexion.
def logout_user(request):
    """Gère la déconnexion de l'utilisateur."""
    logout(request)
    return redirect("login")


# signup_page : Crée le nouveau compte en BDD via form.save().
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


# home : Affiche le flux principal avec les tickets et les critiques combinés.
@login_required
def home(request):
    """Affiche le flux principal de l'utilisateur."""
    tickets = Ticket.objects.all()
    reviews = Review.objects.all()

    # Annotation pour distinguer les types de contenu
    tickets = tickets.annotate(content_type=Value("TICKET", CharField()))
    reviews = reviews.annotate(content_type=Value("REVIEW", CharField()))

    # Combinaison et tri par date de création décroissante
    posts = sorted(
        chain(reviews, tickets), key=lambda post: post.time_created, reverse=True
    )

    context = {
        "posts": posts,
    }
    return render(request, "litrevu/home.html", context)


# ticket_create : Gère la création d'un Ticket seul.
@login_required
def ticket_create(request):
    """Gère la création d'un nouveau ticket."""
    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect("home")
    else:
        form = TicketForm()

    return render(request, "litrevu/ticket_create.html", context={"form": form})


# review_create : Gère la création simultanée d'un Ticket et d'une Critique.
@login_required
def review_create(request):
    """Gère la création d'un ticket et de sa critique associée."""
    ticket_form = TicketForm()
    review_form = ReviewForm()

    if request.method == "POST":
        ticket_form = TicketForm(request.POST, request.FILES)
        review_form = ReviewForm(request.POST)

        if ticket_form.is_valid() and review_form.is_valid():
            # 1. Sauvegarde du Ticket
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()

            # 2. Sauvegarde de la Critique liée
            review = review_form.save(commit=False)
            review.ticket = ticket
            review.user = request.user
            review.save()

            return redirect("home")

    context = {
        "ticket_form": ticket_form,
        "review_form": review_form,
    }
    return render(request, "litrevu/review_create.html", context)
