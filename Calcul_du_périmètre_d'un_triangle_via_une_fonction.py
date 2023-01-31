"""Calcul du périmètre d'un triangle via une fonction"""

print("donner la valeur des 3 côtés")
dimension1=float(input())
dimension2=float(input())
dimension3=float(input())


def Perimeter(dimension1, dimension2, dimension3):
    perimeter = dimension1 + dimension2 + dimension3
    return print("le perimètre est de ", perimeter)
    
Perimeter(dimension1, dimension2, dimension3)