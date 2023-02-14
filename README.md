# OC_Projet_7
Résolvez des problèmes en utilisant des algorithmes en Python
# Créer environnement virtuel "env":
Dans Terminal, à la racine du projet, écrire : python -m venv env
# Activer environnement virtuel "env" :
Dans Terminal, à la racine du projet, écrire : source env/bin/activate

# Installer flake8 et l'utiliser sur les fichiers
Dans Terminal, à la racine du projet, écrire : 
python -m pip install flake8
python -m pip install --upgrade pip
flake8 --filename forcebrute.py --output-file forcebrute_flake-report
flake8 --filename optimized.py --output-file optimized_flake-report

# forcebrute.py 
 * Nous avons besoin que vous conceviez un algorithme qui maximisera le profit réalisé par nos clients après deux ans d'investissement. Votre algorithme doit suggérer une liste des actions les plus rentables que nous devrions acheter pour maximiser le profit d'un client au bout de deux ans.
 * Nous avons les contraintes suivantes :
  - Chaque action ne peut être achetée qu'une seule fois.
  - Nous ne pouvons pas acheter une fraction d'action.
  - Nous pouvons dépenser au maximum 500 euros par client.

# optimized.py
