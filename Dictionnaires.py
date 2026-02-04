student = {
    "John" : 85 ,
    "Alice": 90 ,
    "Bob" : 78 ,
    }

student["amine"] = 65

student["Jonn"] = 95

del student["Bob"]

print("Bob" in student) 

for key, value in student.items():
    print(key,":" , value)
    