"""Création et utilisation d'un tuple"""

data = []
x=5
for i in range (5) :
    x +=3
    data.append(x)
print(data)
save_tuple = (data,) #ici un raccourcis vers la liste est sauvegardé dans le tuple, la liste pourra être éditable mais pas le raccourci. 
print(save_tuple)
print(type(data))
print(type(save_tuple))