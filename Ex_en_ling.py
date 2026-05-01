def add (a,b) :
    return a + b
def sub (a,b) :
    return a + b
def mul (a,b) :
    return a * b
def div (a,b) :
    if b == 0 :
        raise ZeroDivisionError("divisin par 0 impossible")
    return a/ b 
def calculatrice ():
    try:
        a = float(input("entre the fist number :"))
        op = input("enter the opretion(+,-,*,/) : ").strip()
        b= float(input("enter the second number :"))
        operations = {
            "+",
            "-",
            "*",
            "/"
        }
        if op not in operations : 
            raise ValueError("operation invlide")
        resultat = 0
        if op == "+":
            resultat = add(a,b)
        if op == "-":
            resultat = sub(a,b)
        if op == "*":
            resultat = mul(a,b)
        if op == "/":
            resultat = div(a,b)

        return resultat
    except ValueError as e :
        print(e)
    except ZeroDivisionError as e :
        print(e)
print(calculatrice())



# ex 5


# def calculer_panier (**produits):
#     total = 0
#     for nom , prix in produits.items():
#         if prix < 0 :
#             raise ValueError ("price can not be negative")
#         total = total + prix
#     return total
# try:
#     print(calculer_panier(phone=25000, tv=30000, laptop=10000))
# except ValueError as e :
#     print(e)

