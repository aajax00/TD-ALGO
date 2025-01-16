def premier(nbr):
    if nbr <= 1:
        return False # 1 et 0 ne sont pas des nombres premier
    for i in range(2, int(nbr**0.5) + 1): #test des diviseur
        if nbr % 1 == 0:
            return False # si divisible par i = pas nbr premier
    return True # si aucun diviseur trouvé = premier
        

nbr = 18
if premier(nbr):
    print(f"{nbr} est un nombre premier")
else:
    print(f"{nbr} n'est pas un nombre premier")