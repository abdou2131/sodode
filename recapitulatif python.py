# print("student grade analyzer")
# name = input("enter your name :")

# # print ("your name is : " , name)

# etap 

# note_1 = float(input("entre your note_1 :"))
# note_2 = float(input("entre your note_2 :"))
# moyenne = (note_1+note_2) / 2
# # print(moyenne)

# if moyenne >= 10 :
#     print("success")
# elif moyenne >=9 :
#     print("rattrapage")
# else : 
#     print("fail")

# etap 

# print("student grade analyzer")
# name = input("enter your name :")

# note = 0
# while(note != -1):
#     note = (int(input("enter your note :")))

# etap 

# print("student grade analyzer")
# name = input("enter your name :")

# nombredenote = int (input("entr number of notes :"))

# for i in range(nombredenote):
#     note = float(input("enter your note :"))


# etap 



# print("student grade analyzer")
# name = input("enter your name :")

# nombredenote = int (input("entr number of notes :"))

# notes = []
# for i in range(nombredenote):
#     note = float(input("enter your note :"))
#     notes.append(note)
#     print(notes)
# print("final :" , notes)


# etap 

# print("student grade analyzer")
# name = input("enter your name :")

# nombredenote = int (input("entr number of notes :"))

# notes = []
# for i in range(nombredenote):
#     note = float(input("enter your note :"))
#     notes.append(note)
#     print(notes)

# # [12.0, 10.0, 15.0, 16.0, 6.0, 18.0, 14.5, 11.5]
# sum = 0

# for i in range(len(notes)):
#     sum = sum + notes[i]

# print(sum)


# etap 


# print("student grade analyzer")
# name = input("enter your name :")

# nombredenote = int (input("entr number of notes :"))

# notes = []
# for i in range(nombredenote):
#     note = float(input("enter your note :"))
#     notes.append(note)
#     print(notes)

# # [12.0, 10.0, 15.0, 16.0, 6.0, 18.0, 14.5, 11.5]
# sum = 0

# for i in range(len(notes)):
#     sum = sum + notes[i]

# moy = sum / nombredenote
# print ("votre moyenne est : " , moy )



#etap 


# print("student grade analyzer")
# name = input("enter your name :")
# age = input("enter your age :")
# nombredenote = int (input("entr number of notes :"))

# notes = []
# for i in range(nombredenote):
#     note = float(input("enter your note :"))
#     notes.append(note)


# # [12.0, 10.0, 15.0, 16.0, 6.0, 18.0, 14.5, 11.5]
# sum = 0

# for i in range(len(notes)):
#     sum = sum + notes[i]

# moy = sum / nombredenote

# student = {
#     "name" : name , 
#     "Notes" : sum ,
#     "moyanne" : moy
# }
# print (student)


# etap 



print("student grade analyzer")
name = input("enter your name :")
age = input("enter your age :")
nombredenote = int (input("entr number of notes :"))

notes = []
for i in range(nombredenote):
    note = float(input("enter your note :"))
    notes.append(note)
note_minimal = min (notes)
note_maximal = max (notes)
sum = 0

for i in range(len(notes)):
    sum = sum + notes[i]

moy = sum / nombredenote

student = {
    "name" : name , 
    "age" : age ,
    "note minimal" : note_minimal ,
    "note maximal" : note_maximal ,
    "Notes" : sum ,
    "moyanne" : moy
}
print (student)