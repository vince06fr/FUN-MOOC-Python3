# Exercice 2 Semaine 2 FUN-MOOC Python3 de l'UCA
# https://www.fun-mooc.fr/courses/course-v1:UCA+107001+session02/courseware/16fe81d60f134de9a10dd0c44a597584/503146f17dd245bf93ac97e72c03801a/
#
# JRelland 28/01/2020 - https://github.com/JRelland/FUN-MOOC-Python3/
#

# écrivez votre code ici
# Liste qui retourne :
#  None si liste vide
#  Dernier élément si paire
#  Elément du milieu si impaire

def laccess(liste):
    
    if len(liste) == 0:
        # Vide
        print(None)

    elif len(liste) % 2 == 0:
        # Paire 
        return liste[len(liste) - 1]

    else:
        # Impaire
        return liste[len(liste) // 2] 
