"""Import et modification de données via un fichier source version CHATGPT"""

import csv
data=[]
with open("input.csv") as donnees :
    reader = csv.DictReader(donnees, delimiter=',')
    for ligne in reader :
        horaires=int(ligne['heures_travaillees'])
        salaire=str(horaires*15)
        nom=(ligne['nom'])
        temporaire=[nom,salaire]
        data.append(temporaire)
print(data)       
en_tete = ['nom', 'salaire']

with open('output.csv', 'w') as output_csv :
    writer=csv.writer(output_csv, delimiter=',')
    writer.writerow(en_tete)
    for ligne in data:
        writer.writerow(ligne)
        
with open('output.csv', 'w') as output_csv :
    for ligne in data:
        output_csv.write(",".join(ligne).replace(","," ") + "\n")