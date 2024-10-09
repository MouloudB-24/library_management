# Projet  : Gestion de Bibliothèque - Application en ligne de commande

# Objectif
Cette application permet de gérer efficacement des livres papier ou digital ainsi que les utilisateurs d'une 
bibliothèque. Elle facilite l'ajout, l'emprunt et le retour des livres, tout en offrant un suivi des statistiques
historique de livres et utilisateurs.


# Fonctionnalités et mode d'exploitation 
# 1- Gestion de la bibliothèque
**Creation de la bibliothèque :** créer le bibliothèque, via la commande : `python3 main.py create-library`

# 2- Gestion des livres
**Ajout un livre :** ajouter un livre (papier ou digital) à la bibliothèque, via la commande : `python3 main.py add-book`
**Spprimer un livre :** supprimer un livre à la bibliothèque, via la commande : `python3 main.py delete-book`
**Emprunter un livre :** emprunter un livre à la bibliothèque, via la commande : `python3 main.py borrow-book`
**Retourner un livre :** retourner un livre à la bibliothèque, via la commande : `python3 main.py return-book`
**Chercher un livre :** chercher un livre à la bibliothèque avec son ISBN, via la commande : `python3 main.py search-book`
**Mis à jour un livre :** mettre à jour un livre à la bibliothèque, via la commande : `python3 main.py update-book`
**Consulter des livres :** consulter tous les livres disponbles à la bibliothèque, via la commande : `python3 main.py all-books`
**Consulter le classement des livres :** consulter les livres les mieux empruntés à la bibliothèque, via la commande : `python3 main.py top-books`

# 3- Gestion des utilisateurs
**Ajout un utilisateur :** inscrire un utilisateur à la bibliothèque, via la commande : `python3 main.py add-user`
**Supprimer un utilisateur :** supprimer un utilisateur de la bibliothèque, via la commande : `python3 main.py delete-user`
**Consulter des utilisateurs :** consulter tous les utilisateurs inscrit à la bibliothèque, via la commande : `python3 main.py all-users`
**Consulter le classement des utilisateurs :** consulter les utilisateurs qui empruntent plus de livres à la bibliothèque, via la commande : `python3 main.py top-users`

# Remarques : 
Avant d'utiliser les autres fonctionnalités, il est fortement recommandé de commencer par créer la bibliothèque en exécutant la commande :
`python3 main.py create-library`
Pour obtenir une liste complète des commandes disponibles et leur description, vous pouvez consulter l'aide en exécutant :
`python3 main.py --help`

# Installation :
1. Ouvrez le terminal ou l'invite de commandes selon votre _OS_.

2. Clonez le répertoire avec la commande : `git clone git@github.com:MouloudB-24/library_management.git`

3. Accédez au répertoire avec la commande : `cd library_management`

4. Créer un environement virtuel avec cette commande : `python3 -m venv env`
`
5. Activez l'environnement virtuel avec cette commande : `source env/bin/activate`

5. Installez les dépendances avec la commande : `pip install -r requirements.txt`
    
5. Lancez la commande d'aide : `python3 main.py --help`

Usage: main.py [OPTIONS] COMMAND [ARGS]...                                                                                              
╭─ Options ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --install-completion          Install completion for the current shell.                                                              │
│ --show-completion             Show completion for the current shell, to copy it or customize the installation.                       │
│ --help  

╭─ Commands ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ add-book         Command to add a book.                                                                                              │
│ add-user         Command to add a user.                                                                                              │
│ all-books        Command to get all books.                                                                                           │
│ all-users        Command to get all users.                                                                                           │
│ borrow-book      Command to borrow a book.                                                                                           │
│ create-library   Command to crete a library.                                                                                         │
│ delete-book      Command to delete a book.                                                                                           │
│ delete-user      Command to delete a user.                                                                                           │
│ return-book      Command to return a book.                                                                                           │
│ search-book      Command to search a book.                                                                                           │
│ top-books        Command to get top books.                                                                                           │
│ top-users        Command to get top users.                                                                                           │
│ update-book      Command to update a book.  

**Nota :** Assurez-vous d'avoir un environnement Python configuré.