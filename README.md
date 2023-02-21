# OC_Projet_7
Résolvez des problèmes en utilisant des algorithmes en Python
# Créer environnement virtuel "env":
Dans Terminal, à la racine du projet, écrire : python -m venv env
# Activer environnement virtuel "env" :
Sur Windows : dans le terminal, à la racine du projet, écrire : source env/Scripts/activate
Sur Mac ou Linux : dans le terminal, à la racine du projet, écrire : source env/bin/activate

# Installer flake8 et l'utiliser sur les fichiers
Dans Terminal, à la racine du projet, écrire : 
pip install -r requirements.txt
flake8 --format=html --htmldir=flake-report
