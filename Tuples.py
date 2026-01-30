#  Exercice :01
# jours = ('dimanche' , 'lundi' , 'mardi' , 'mercredi' , 'jeudi' , 'vendredi' , 'samedi' )
# Taches =[]

# for jour in jours :
#     tache = input('Entrez votre tache ici : ')
#     Taches.append(tache)

# for i in range(7):
#     print(jours[i] , ':' , Taches [i] )

jours = ('dimanche' , 'lundi' , 'mardi' , 'mercredi' , 'jeudi' , 'vendredi' , 'samedi' )
Taches =[]

for jour in jours :
    tache = input('Entrez votre tache ici : ')
    Taches.append(tache)

for i in range(len(jours)):
    print(jours[i] , ':' , Taches [i] )