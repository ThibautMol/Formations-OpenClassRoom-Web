"""Edition et copie d'une liste initiale"""

a = [1, 2, 3]
b = a.copy() #la copie permet de reprendre le contenue des données et non pas de créer un raccourcis vers la liste
print(a)
a.append(4)
print(a)
print(b)#une liste dans un tuple peut être modifiée en passant par la modification de la liste.