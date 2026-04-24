# def safe_division():
#     try:
#         a = int(input("Enter a number:"))
#         b = int(input("Enter another number:"))
#         print(a / b)
#     except ZeroDivisionError:
#         print("Impossible de diviser par zéro")
#     except ValueError:
#         print("Entrée invalide")
# safe_division()



def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Solde insuffisant")
    return balance - amount

try:
    withdraw(1000,20000)
except ValueError as e:
    print(e)