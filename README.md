# LITRevu - Plateforme de Critiques Littéraires

Ce projet est développé dans le cadre de la formation Développeur d'Application Python. L'objectif est de créer une application web permettant aux utilisateurs de solliciter ou de publier des critiques de livres ou d'articles.

---

## 🚀 Étape 1 : Initialisation et Authentification

Cette première phase a consisté à mettre en place l'architecture globale du projet Django et à isoler la gestion des utilisateurs de manière évolutive.

### 🛠️ Fonctionnalités réalisées
* **Initialisation du projet Django** : Création du dossier de configuration global `litrevu_project`.
* **Application `authentication`** : Création d'une application dédiée à la gestion des accès (connexion, inscription).
* **Modèle Utilisateur Personnalisé** : Implémentation d'une classe `User` héritant de `AbstractUser` dès le premier jour pour anticiper les futures évolutions de la base de données.
* **Base de données & Superuser** : Exécution des migrations initiales (SQLite) et configuration du compte administrateur.

---

## 📚 Étape 2 : Modèles de Données (Core)

Mise en place du cœur de l'application avec la création des modèles nécessaires aux fonctionnalités de critiques littéraires et d'abonnements.

### 🛠️ Fonctionnalités réalisées
* **Application `litrevu`** : Création de l'application principale du projet.
* **Modèle `Ticket`** : Permet aux utilisateurs de demander une critique en renseignant un titre, une description et une image de couverture.
* **Modèle `Review`** : Permet de publier une critique liée à un Ticket, avec un système de note (0 à 5), un titre et un corps de texte.
* **Modèle `UserFollows`** : Gestion du système d'abonnements croisés entre utilisateurs avec contrainte d'unicité pour éviter les doublons.
* **Gestion des Médias** : Intégration de la bibliothèque Pillow pour la gestion des fichiers images des tickets.

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

# Installer les dépendances
pip install -r requirements.txt
```

### 3. Base de données et Serveur
```bash

# Appliquer les migrations
python manage.py migrate
# Lancer le serveur de développement
python manage.py runserver




👤 Auteur Kevin Delcroix
2026