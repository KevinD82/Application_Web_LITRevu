from itertools import chain

from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import CharField, Value
from django.shortcuts import get_object_or_404, redirect, render

from litrevu.models import Review, Ticket, UserFollows

from .forms import LoginForm, ReviewForm, SignupForm, TicketForm

User = get_user_model()

# --- AUTHENTIFICATION ---

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


# --- FLUX & POSTS ---

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


@login_required
def posts(request):
    """Affiche les publications créées par l'utilisateur connecté."""
    user_tickets = Ticket.objects.filter(user=request.user).annotate(
        content_type=Value("TICKET", CharField())
    )
    user_reviews = Review.objects.filter(user=request.user).annotate(
        content_type=Value("REVIEW", CharField())
    )

    user_posts = sorted(
        chain(user_reviews, user_tickets),
        key=lambda post: post.time_created,
        reverse=True,
    )

    context = {
        "posts": user_posts,
    }
    return render(request, "litrevu/posts.html", context)


# --- ABONNEMENTS ---

@login_required
def subscriptions(request):
    """Affiche la page de gestion des abonnements et gère le suivi d'utilisateurs."""
    message = ""

    if request.method == "POST":
        username_to_follow = request.POST.get("username")
        if username_to_follow:
            try:
                user_to_follow = User.objects.get(username=username_to_follow)

                if user_to_follow == request.user:
                    message = "Vous ne pouvez pas vous suivre vous-même."
                else:
                    UserFollows.objects.get_or_create(
                        user=request.user,
                        followed_user=user_to_follow
                    )
                    return redirect("subscriptions")
            except User.DoesNotExist:
                message = f"L'utilisateur '{username_to_follow}' n'existe pas."

    following = UserFollows.objects.filter(user=request.user)
    followers = UserFollows.objects.filter(followed_user=request.user)

    context = {
        "following": following,
        "followers": followers,
        "message": message,
    }
    return render(request, "litrevu/subscriptions.html", context)


@login_required
def unsubscribe(request, follow_id):
    """Permet de supprimer un abonnement."""
    follow = get_object_or_404(UserFollows, id=follow_id, user=request.user)
    if request.method == "POST":
        follow.delete()
        return redirect("subscriptions")
    return redirect("subscriptions")


# --- CREATION TICKETS & CRITIQUES ---

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


@login_required
def review_create(request):
    """Gère la création d'un ticket et de sa critique associée."""
    ticket_form = TicketForm()
    review_form = ReviewForm()

    if request.method == "POST":
        ticket_form = TicketForm(request.POST, request.FILES)
        review_form = ReviewForm(request.POST)

        if ticket_form.is_valid() and review_form.is_valid():
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()

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


@login_required
def review_create_reply(request, ticket_id):
    """Gère la création d'une critique en réponse à un ticket existant."""
    ticket = get_object_or_404(Ticket, id=ticket_id)
    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            return redirect("home")
    else:
        review_form = ReviewForm()

    return render(
        request,
        "litrevu/review_create.html",
        {"review_form": review_form, "ticket": ticket},
    )


# --- MODIFICATION ET SUPPRESSION DES TICKETS ---

@login_required
def ticket_update(request, ticket_id):
    """Permet à l'utilisateur de modifier son ticket."""
    ticket = get_object_or_404(Ticket, id=ticket_id, user=request.user)
    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect("posts")
    else:
        form = TicketForm(instance=ticket)

    return render(
        request,
        "litrevu/ticket_create.html",
        {"form": form, "edit_mode": True},
    )


@login_required
def ticket_delete(request, ticket_id):
    """Permet à l'utilisateur de supprimer son ticket."""
    ticket = get_object_or_404(Ticket, id=ticket_id, user=request.user)
    if request.method == "POST":
        ticket.delete()
        return redirect("posts")

    return render(request, "litrevu/ticket_delete.html", {"ticket": ticket})


# --- MODIFICATION ET SUPPRESSION DES CRITIQUES ---

@login_required
def review_update(request, review_id):
    """Permet à l'utilisateur de modifier sa critique."""
    review = get_object_or_404(Review, id=review_id, user=request.user)
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect("posts")
    else:
        form = ReviewForm(instance=review)

    return render(
        request,
        "litrevu/review_create.html",
        {"review_form": form, "ticket": review.ticket, "edit_mode": True},
    )


@login_required
def review_delete(request, review_id):
    """Permet à l'utilisateur de supprimer sa critique."""
    review = get_object_or_404(Review, id=review_id, user=request.user)
    if request.method == "POST":
        review.delete()
        return redirect("posts")

    return render(request, "litrevu/review_delete.html", {"review": review})