# LITRevu - Plateforme de Critiques Littéraires

Ce projet est développé dans le cadre de la formation Développeur d'Application Python. L'objectif est de créer une application web permettant aux utilisateurs de solliciter ou de publier des critiques de livres ou d'articles.

---

## 🚀 Étape 1 : Initialisation et Authentification

Cette première phase a consisté à mettre en place l'architecture globale du projet Django et à isoler la gestion des utilisateurs de manière évolutive.

### 🛠️ Fonctionnalités réalisées
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

## 🔄 Étape 3 : Flux d'actualités et Système d'Abonnements

Mise en place de la logique métier permettant aux utilisateurs d'interagir entre eux et de consulter un flux centralisé.

### 🛠️ Fonctionnalités réalisées
* **Flux personnalisé (`Flux`)** : Affichage dynamique de tous les tickets et critiques créés par l'utilisateur connecté ainsi que par les utilisateurs qu'il suit.
* **Page "Vos posts"** : Interface dédiée regroupant uniquement les tickets et les critiques publiés par l'utilisateur connecté pour faciliter leur gestion (modification et suppression).
* **Gestion des abonnements** : 
  * Page de recherche et d'ajout d'utilisateurs à suivre.
  * Liste interactive des abonnements en cours et des abonnés.
  * Possibilité de se désabonner à tout moment.

---

## ✍️ Étape 4 : Gestion des Tickets et des Critiques (CRUD)

Implémentation complète des interfaces permettant la création, la lecture, la modification et la suppression des contenus littéraires.

### 🛠️ Fonctionnalités réalisées
* **Création de Ticket seul** : Formulaire permettant de demander une critique sur un livre ou un article.
* **Création de Critique seule** : Formulaire pour répondre à un ticket existant (notation de 0 à 5 et commentaire).
* **Création combinée (Ticket + Critique)** : Formulaire unique permettant de poster simultanément un nouveau ticket et sa critique associée.
* **Modification et Suppression** : Sécurisation des vues pour que seuls les auteurs respectifs puissent modifier ou supprimer leurs tickets et critiques.

---

## 🧪 Étape 5 : Tests et Qualité du Code

Validation du bon fonctionnement de l'application à l'aide de tests unitaires et fonctionnels.

### 🛠️ Fonctionnalités réalisées
* **Tests des Modèles** : Vérification du comportement des champs, des méthodes personnalisées et des contraintes d'unicité (notamment pour `UserFollows`).
* **Tests des Vues et Formulaires** : Validation des codes de statut HTTP, des redirections, des accès restreints (utilisateurs non connectés) et de la soumission correcte des formulaires.
* **Vérification de la couverture** : Utilisation de l'outil `coverage` pour s'assurer d'un taux de couverture de code satisfaisant.

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
```


👤 Auteur Kevin Delcroix
2026
