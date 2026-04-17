def calculer_HT(prix, quntite):
    prix_HT= (prix * quntite)
    return prix_HT

def taxe (prix_Ht , tax):
    prix_tax= (prix_Ht * tax)
    return prix_tax


def prix_total (prix , quntite , tax= 0.19 ):
    prix_ht = calculer_HT(prix , quntite )
    prix_taxe = taxe(prix_ht, tax )
    return prix_ht + prix_taxe

print (prix_total(100 , 2))