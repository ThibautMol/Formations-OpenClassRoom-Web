"""Edition et copie d'une liste initiale V.2"""

liste_originale = [1, 2, 3]

# Copies
liste_originale_referencee = liste_originale
liste_originale_copiee = liste_originale.copy() #création d'une nouvelle liste et non reprise d'un raccourcis vers la liste originale.

#Modification de la liste originale
liste_originale.append("j'ai été modifiée")

print("...........liste_originale :", liste_originale)
print("liste_originale_referencee :", liste_originale_referencee)
print("....liste_originale_copiee :", liste_originale_copiee)
print(type(liste_originale_copiee))