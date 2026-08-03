# LITRevu - Plateforme de Critiques Littéraires

LITRevu est une application web développée avec le framework **Django**. Elle permet à une communauté de passionnés de lecture de demander, publier et consulter des critiques de livres ou d'articles littéraires.

---

## 🛠️ Fonctionnalités de l'application

### 🔐 Authentification & Sécurité
* **Gestion des accès** : Pages de connexion, d'inscription et de déconnexion.
* **Accès protégé** : Les pages intérieures de l'application sont réservées aux utilisateurs connectés.
* **Modèle utilisateur personnalisé** : Utilisation d'un modèle d'utilisateur étendu pour anticiper les évolutions futures.

### 📰 Flux d'actualités & Publications
* **Fil d'actualité (`Home`)** : Affichage antéchronologique des tickets et critiques publiés par l'utilisateur ainsi que par les personnes qu'il suit.
* **Page "Vos posts"** : Interface centralisant uniquement les créations de l'utilisateur pour en faciliter la gestion.

### 👥 Système d'abonnements
* **Recherche et suivi** : Possibilité de rechercher un utilisateur par son nom exact pour s'abonner à ses publications.
* **Gestion du réseau** : Visualisation de la liste de ses abonnements/abonnés et possibilité de se désabonner en un clic.

### ✍️ Gestion du contenu (CRUD)
* **Création de ticket** : Formulaire pour solliciter une critique sur un livre (avec possibilité d'ajouter une image de couverture).
* **Création de critique** : Possibilité de répondre à un ticket existant ou de créer simultanément un ticket et sa critique.
* **Modification et suppression** : Contrôle strict permettant à chaque utilisateur de modifier ou supprimer uniquement ses propres publications.

---

## 💻 Installation et Lancement local

### 1. Prérequis
* Python 3.x
* Git

### 2. Configuration de l'environnement
```bash

# Création de l'environnement virtuel
python -m venv env

# Activer l'environnement virtuel (Windows)
.\env\Scripts\activate

# Activer l'environnement virtuel (Mac / Linix)
source env/bin/activate

# Installer les dépendances
pip install -r requirements.txt
```

### 3. Base de données et Serveur
```bash

# Appliquer les migrations
python manage.py migrate

# Lancer le serveur de développement
python manage.py runserver
```


👤 Auteur Kevin Delcroix
2026
