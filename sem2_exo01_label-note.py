# Exercice 1 Semaine 2 FUN-MOOC Python3 de l'UCA
# https://www.fun-mooc.fr/courses/course-v1:UCA+107001+session02/courseware/16fe81d60f134de9a10dd0c44a597584/503146f17dd245bf93ac97e72c03801a/
#
# JRelland 28/01/2020 - https://github.com/JRelland/FUN-MOOC-Python3/
#

# à vous de jouer
# Résultat des notes
## 0⩽𝑛𝑜𝑡𝑒<10     '{prenon} est recalé'
## 10⩽𝑛𝑜𝑡𝑒<16    '{prenon}  est reçu'
## 16⩽𝑛𝑜𝑡𝑒⩽20    'féliciations à {prenon}'

def label(prenom, note):
    if note < 0 or note > 20:
        return f"La note de {prenom} doit être en 0 et 20."
    
    elif note < 10:
        # cas recalé
        return f"{prenom} est recalé"
        
    elif note < 16:
        # Cas reçu
        return f"{prenom} est reçu"
    
    else:
        # Cas félicitations
        return f"félicitations à {prenom}"