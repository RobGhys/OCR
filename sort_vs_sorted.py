"""
Sort
"""
prenoms = ["Jacques", "Laure", "André", "Victoire", "Albert", "Sophie"]
prenoms.sort()
print(prenoms)

"""
Sorted retourne un nouvel objet
Sorted fonctionne sur tous les types de séquence (tuple, liste, dictionnaire)
Option : reverse=True
"""
prenoms = ["Jacques", "Laure", "André", "Victoire", "Albert", "Sophie"]
sorted(prenoms)
print(prenoms)
prenoms_copy = sorted(prenoms)
print("---   SORTED   ---")
print(prenoms_copy)

"""
Dictionnary : tri sur base de la clé
"""

# Prénom, Age, Moyenne
etudiants = [
    ("Clément", 14, 16),
    ("Charles", 12, 15),
    ("Oriane", 14, 18),
    ("Thomas", 11, 12),
    ("Damien", 12, 15),
]

print(sorted(etudiants))

# Tri sur base de la moyenne
etu_tri_moyenne = sorted(etudiants, key=lambda colonnes: colonnes[2])
print(etu_tri_moyenne)

"""
Idem en OO
"""

class Etudiant:

    """Classe représentant un étudiant.

    On représente un étudiant par son prénom (attribut prenom), son âge
    (attribut age) et sa note moyenne (attribut moyenne, entre 0 et 20).

    Paramètres du constructeur :
        prenom -- le prénom de l'étudiant
        age -- l'âge de l'étudiant
        moyenne -- la moyenne de l'étudiant

    """

    def __init__(self, prenom, age, moyenne):
        self.prenom = prenom
        self.age = age
        self.moyenne = moyenne

    def __repr__(self):
        return "<Étudiant {} (âge={}, moyenne={})>".format(
                self.prenom, self.age, self.moyenne)

etudiants = [
    Etudiant("Clément", 14, 16),
    Etudiant("Charles", 12, 15),
    Etudiant("Oriane", 14, 18),
    Etudiant("Thomas", 11, 12),
    Etudiant("Damien", 12, 15),
]

etu_oo_tri_moyenne = sorted(etudiants, key=lambda etudiant: etudiant.moyenne)
print(etu_tri_moyenne)

"""
Fonction Module Operator appliquée sur une liste de tuples
"""

etudiants = [
    ("Clément", 14, 16),
    ("Charles", 12, 15),
    ("Oriane", 14, 18),
    ("Thomas", 11, 12),
    ("Damien", 12, 15),
]

from operator import itemgetter
# Fait la même chose que Lambda + sorted
print(sorted(etudiants, key=itemgetter(2)))