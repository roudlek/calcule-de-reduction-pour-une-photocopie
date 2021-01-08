drp = False
reduction = 0
Nbp = int(input("entrer le nombre des pages : "))
if Nbp <= 10 and Nbp > 0 :
    reduction = 0
elif Nbp > 10 and Nbp < 20 :
    reduction = 0.3
elif Nbp >= 20 :
    reduction = 0.6
else:
    drp = True
    print("Le nombre saisis est incorrect !!")
if Nbp > 0 :
    Facture = 0.5 * Nbp * (1-reduction)
    print("La facture est",Facture)
