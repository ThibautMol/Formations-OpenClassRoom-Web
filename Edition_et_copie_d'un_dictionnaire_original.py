"""Edition et copie d'un dictionnaire original"""

dico_original = {"a": "a", "b": "b"}

# Copies
dico_original_referencee = dico_original
dico_original_copiee = dico_original.copy()

#Modification de la variable dico original
dico_original["c"] = "c"

print("...........dico_original :", dico_original)
print("dico_original_referencee :", dico_original_referencee)
print("....dico_original_copiee :", dico_original_copiee)