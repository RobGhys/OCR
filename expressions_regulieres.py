import re

expression_2 = 'chat'
chaine_2 = 'chaton lol mdr'

if re.match(expression_2, chaine_2) is not None:
    # Si l'expression est dans la chaîne
    pass
    # Ou alors, plus intuitivement
if re.match(expression_2, chaine_2):
    pass

re.search(r"abc", "abcdef")
re.search(r"abc", "abacadaeaf")
re.search(r"abc*", "ab")
re.search(r"abc*", "abccc")
re.search(r"chat*", "chateau")


chaine_2 = ""
# ^: début de la chaîne
# $: fin de la chaîne
# 0: trouver un zéro
# [0-9]: un chiffre entre 0 et 9
# ( ... ): un groupe
# [ .-] : soit ' ', soit '.', soit '-'
# ?: la classe qui précède, càd [ .-] est optionnelle
# [0-9]{2}: on attend deux chiffres entre 0 et 9
# {4} tout le groupe ( ... ), càd un séparateur ' .-' optionnel + deux chiffres, est répété 4x
expression_2 = r"^0[0-9]([ .-]?[0-9]{2}){4}$"
while re.search(expression_2, chaine_2) is None:
    chaine_2 = input("Saisissez un numéro de téléphone (valide) :")


'''On peut aussi stocker ces expressions dans des variables compilées'''
chn_mdp = r"^[A-Za-z0-9]{6,}$"
exp_mdp = re.compile(chn_mdp)