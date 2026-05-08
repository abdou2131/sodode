# etudiant = {
#     "John" : 15 ,
#     "Alice": 16 ,
#     "amina" : 14 ,
#     "amar" : 9 ,
#     "morad" : 8 ,
#     "samira" : 16 ,
#     "abdou" : 18
#     }
# def afeche_etudiant ():
#     for key, value  in etudiant.items():
#         print(key ,value)

# def max_not ():
#     max_note = -1
#     for key , value in etudiant.items() :
#         if max_note <value :
#             max_note = value
#     return (key , max_note)
# print(max_not())

# def eleves_admis ():
#     for key, value  in etudiant.items():
#         if value >= 10  :
#             print (key , value)

# eleves_admis ()

# def modifier_note ():
#     nom = input("enter le nom de l'etudiant : ")
#     note = float(input("enter la note : "))
#     etudiant[nom] = note
#     afeche_etudiant()
# modifier_note()

# def nouvel_etudi ():
#     nom = input("enter le nom de l'etudiant : ")
#     note = float(input("enter la note : "))
#     etudiant[nom] = note
#     nouvel_etudi()
# modifier_note()



# EX 02 
# livres_bibliothèque = {
#     "Les Misérables" : 5,
#     "Le Petit Prince" : 6,
#     "L'Étranger" : 0,
#     "La Bibliothèque de minuit ": 3,
#     "Madame Bovary" : 4,
#     "Le Rouge et le Noir " : 12,
#     "Crime et Châtiment " : 10
#     }
# def afeche_livresN ():

#     nom_livre = input("enter le nom du livres : ")
#     if nom_livre not in livres_bibliothèque : 
#         raise ValueError("livre non execte")
#     if livres_bibliothèque[nom_livre] == 0 :
#         raise ValueError("livre sorte")
#     livres_bibliothèque[nom_livre] = livres_bibliothèque[nom_livre] -1
#     print (livres_bibliothèque)
    
# try :
#     (afeche_livresN())
# except ValueError as e :
#     print (e)