"""Manipulation d'une liste avec des méthodes"""

guests = []
guests.append('Joey')
guests.append('Martin')
guests.append('Mary')
guests.extend(['bob', 'bernard', 'kevin'])
print(len(guests))
print(guests)
guests[1] ='John'
guests.remove("Joey")
for guest in guests:
    print(guest)