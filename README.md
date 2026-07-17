# AlgoInvest&Trade - Optimisation de Portefeuille Financier

Ce projet a été développé pour **AlgoInvest&Trade**, une société financière spécialisée dans l'investissement. L'objectif est de concevoir un algorithme d'optimisation permettant de maximiser le profit des clients sur un investissement à court terme (2 ans), sous contrainte de budget (500 € maximum par client).

Chaque action ne peut être achetée qu'une seule fois et l'achat de fractions d'actions est impossible (Problème du sac à dos 0/1).

---

## 📁 Structure du Projet

Le projet respecte les conventions de nommage des livrables et est structuré de la manière suivante :

*   `bruteforce.py` : Script contenant l'algorithme de force brute (recherche de la solution optimale absolue par exploration exhaustive).
*   `optimized.py` : Script optimisé contenant la phase de nettoyage des données (Pandas) et le comparatif des deux algorithmes d'optimisation (Glouton vs Programmation Dynamique).
*   `data/` : Dossier contenant les fichiers de données d'entrée au format CSV (les jeux de données fournis et historiques).
*   `README.md` : Guide d'utilisation et de compréhension du projet (ce fichier).

---

## 🛠️ Algorithmes Implémentés

### 1. Force Brute (`bruteforce.py`)
*   **Principe :** Utilise `itertools.combinations` pour explorer absolument $2^N$ combinaisons possibles d'actions.
*   **Complexité Temporelle :** $O(2^N)$ (Exponentielle).
*   **Limite :** Inutilisable au-delà de 20 à 30 actions en raison de l'explosion du temps de calcul et de la mémoire requise.

### 2. Algorithme Glouton (`optimized.py`)
*   **Principe :** Trie les actions par leur ratio d'efficacité ($\text{profit} / \text{coût}$) de manière décroissante et sélectionne les meilleures qui respectent le budget.
*   **Complexité Temporelle :** $O(N \log N)$ (Quasi-linéaire).
*   **Avantage :** Réponse instantanée (quelques millisecondes), idéal pour le traitement en temps réel de volumes massifs d'actions.
*   **Limite :** Ne garantit pas systématiquement l'optimum absolu à 100 % (solution approchée extrêmement proche de l'optimum).

### 3. Programmation Dynamique (`optimized.py`)
*   **Principe :** Résout le problème du sac à dos exact en construisant une matrice d'aide à la décision. Les prix étant décimaux, ils sont convertis en centimes d'euros (entiers) pour créer les indices de la grille.
*   **Complexité Temporelle :** $O(N \times W)$ (où $W$ représente le budget de 50 000 centimes).
*   **Avantage :** Garantit la solution optimale absolue au centime près.
*   **Limite :** Consommation de RAM et temps de calcul plus élevés que l'algorithme glouton (6 à 12 secondes sur les grands jeux de données).

---

## ⚙️ Installation et Prérequis

Ce projet requiert **Python 3** et la bibliothèque **Pandas** pour le nettoyage de données.

### 1. Cloner le projet et se positionner dans le dossier
```bash
git clone <url_du_depot>
cd <nom_du_projet>
```

### 2. Installer les dépendances
```bash
# Création de l'environnement virtuel
python -m venv env

# Activation de l'environnement (Windows)
env\Scripts\activate
# Activation de l'environnement (macOS/Linux)
source env/bin/activate

# Installation de Pandas
pip install -r requirements.txt

### 3. Placer les fichiers de données
```
Assurez-vous que vos fichiers de données CSV sont correctement placés dans le dossier data/
```
- data/liste_actions.csv (pour la force brute)

- data/dataset1_Python+P7.csv (pour l'optimisé)

- data/dataset2_Python+P7.csv (pour l'optimisé)
```

### 4. Utilisation

Exécuter l'algorithme de Force Brute
```Bash
python bruteforce.py
```

Exécuter les algorithmes optimisés (Comparatif Glouton vs Dynamique)
```Bash
python optimized.py
```

👤 Auteur Kevin Delcroix
2026