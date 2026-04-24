#  Exercice :01

# with open("test.txt", "w") as file:
#     file.write("ATOUI Abdessamed")
# file.close()




#  Exercice :02

# file = open("test.txt", "r")
# content = file.read()
# print(content)
# file.close()




#  Exercice :03

# with open("test.txt", "a") as file:
#     file.write("age : 44\n")
# file.close()




#  Exercice :04

# with open("numbers.txt", "w") as file:
#     file.write("1\n")
#     file.write("2\n")
#     file.write("3\n")
#     file.write("4\n")
#     file.write("5\n")
# file.close()




#  Exercice :05

# file = open("numbers.txt", "r")
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# file.close()

# #  ou 

# file = open("numbers.txt", "r")
# for i in range(0,5) : 
#     print(file.readline())

# file.close()




# Exercice : 06

# name1 = input("enter your name1: ")
# name2 = input("enter your name2: ")
# name3 = input("enter your name3: ")
# with open("names.txt", "w") as file:
#     file.write(name1)
#     file.write("\n")
#     file.write(name2)
#     file.write("\n")
#     file.write(name3)

# file.close()


# ou

# name=[]
# for i in range(3):
#     name1 = input("enter your name: ") 
#     name.append(name1)
# with open("names1.txt", "w") as file:
#      for i in range(0 , 3): 
#         file.write(name[i])
#         file.write("\n")
# file.close()



# Exercice : 07

# name=[]
# file = open("names.txt", "r")
# for i in range(3):
#     name.append(file.readline())
    
# file.close()
# print(name)

# ou

# ??????




# Exercice : 07







# avoir

# Chemin de votre fichier

# fichier = "numbers.txt"

# # Lecture du fichier et stockage dans une liste
# with open(fichier, "r", encoding="utf-8") as f:
#     lignes = f.readlines()

# # Optionnel : Enlever les caractères de saut de ligne '\n'
# lignes = [ligne.strip() for ligne in lignes]

# print(lignes)

count = 0
file = open("numbers.txt", "r")
for line in file:
        count +=1
print(count)

