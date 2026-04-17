# def say_hello():
#     print('Hello')

# 1

# def greet(name):     #paramétre
#     print("Hello" , name)
# greet("ahmed") #argument 
# greet("amina")
# greet("omar")

# 2 plusieurs paramétre

# def add(a,b):
#     print(a+b)

# add(3,5)


# 3 return vs print (Trèms important)


# def add(a, b) : 
#     return a + b

# result = add(2, 3)

# print (result)



# 3 paramètres par défaut


# def greet(name = "Guest"):
#     print("Hello", name)

# greet()
# greet("Omer")

# 4 Arguments nommés (Keyword Arguments)

# def student(name , age):
#     print(name , age)

# student (age=20 , name = "ali")

# 5 Argument varriables

# def sum_all(*numners):
#     total = 0 
#     for n in numners :
#         total += n
#     return total
# result = sum_all(1, 2, 3,4)
# print(result)

#6 (arguments nommés variables) 

# def show_info(**data):
#     # print(data)
#     for key, value in data.items():
#         print(key,":", value)
# # show_info(name="Ali" , age=20)
# show_info(name="Ali" , age=20 , heigth=1.0)

# 7 Scope (Portée des variables)   locale and globale

# 8 Fonctions lamda 

# add = lambda a ,b : a+b
# print(add(2,3))

# nums = [1, 2, 3, 4]
# resulta = list(map(lambda x : x * 2 , nums))
# print (resulta)

def claculate_price(price, tax):
    return price + price * tax

def print_invoice(name , price , tax = 0.19):
    total = claculate_price(price,tax)
    print("Clint:", name)
    print("Total :" , total)
print_invoice("ahmed" , 1500, 0.22)
print_invoice("omar" , 1200 )