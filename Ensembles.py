# EX 01
Math = {"John", "Alice" , "Bob" , "Charlie" }
Physique = {"Alice" , "David" , "Charlie" , "Emma"}

Math.add("amine")
Physique.add("amal")

Math.remove("Bob")

intersection_set = Math & Physique

union_set = Math|Physique 

difference_set = Math - Physique

symétrique_différence = Math ^ Physique

print ("intersection" , intersection_set)

print ("union" , union_set)

print ("difference" , difference_set)

print ("symétriquedifférence" , symétrique_différence)
