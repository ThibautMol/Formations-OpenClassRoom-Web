"""Utilisation d'une liste avec les méthodes .choice et .sample"""

import random

liste = ['red', 'blue', 'yellow', 'brown', 'pink', 'black', 'white', 'orange']
x=len(liste)
for i in range (0,x) :
    print(random.choice(liste))
y=x//2
print("seconde partie")
for i in range (0,y) :
    print(random.sample(liste,y)) #y permet ici de dire le nombre d'éléments à tirer par tirage (souvent appelé 'k'))