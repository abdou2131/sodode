
# #  ex1
# prices =[]
# def add_tiem():
#     while True : 
#         price = float(input("enter a price : "))
#         if price == 0 :
#             break
#         prices.append(price)
# add_tiem()

# def calculat_price ():
#     total = 0
#     for price in prices :
#         total = total + price
#     return total

# def show_summary ():
#     print(calculat_price())
#     print (len(prices))
#     print (max(prices))
# show_summary ()


# def count_plus_cent ():
#     count = 0
#     for price in prices :
#         if price > 100 :
#             count=count+1
#     return count
# print(count_plus_cent())   

# chatGPT

# def add_item(prices):
# # """Ajoute un prix à la liste"""
#     price = float(input("Entrez le prix de l'article (0 pour terminer) : "))
#     return price


# def calculate_total(prices):
# # """Calcule le prix total"""
#     return sum(prices)


# def show_summary(prices):
# # """Affiche le résumé"""
#     if not prices:
#         print("Aucun article saisi.")
#         return
    
#     total = calculate_total(prices)
#     count = len(prices)
#     max_price = max(prices)

#     print("\n--- Résumé ---")
#     print(f"Prix total : {total:.2f} ")
#     print(f"Nombre d'articles : {count}")
#     print(f"Article le plus cher : {max_price:.2f}")


# def main():
#     prices = []

#     while True:
#         price = add_item(prices)
#         if price == 0:
#             break
#         prices.append(price)

#     show_summary(prices)


# # Lancer le programme
# main()



# ex 2

notes = []
def notes_list():
    while True :
        note = float(input("enter la note : "))
        if note == -1 :
            break
        notes.append(note)
notes_list()
print ("la liste des notes :", notes )

def moyenne_list():
    sum = 0
    for note in notes :
    
        sum = sum + note 
        moyenne = sum / (len(notes))
    return moyenne
print ("la moyenne : " , moyenne_list ())

def note_elevee ():

    print("la note la plus elevee : " , max(notes))
note_elevee()

def note_basse():

    print("la note la plus basse : " , min(notes))
note_basse()

def eleves_admis ():
    count = 0
    for note in notes :
        if note >= 10  :
            count = count + 1
    return count
print("le nombre d'eleves admis :" , eleves_admis())  

def eleves_ajournes ():
    count = 0
    for note in notes :
        if note < 10  :
            count = count + 1
    return count
print("le nombre d'eleves ajourbes :" , eleves_ajournes()) 


