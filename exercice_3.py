def somme_cube(nbr):
    somme = sum(int(chiffre) ** 3 for chiffre in str(nbr))
    return somme
    
#somme des cube plus detaillé
def somme_des_cubes(nbr):
    chiffres = str(nbr)
    somme = 0
    for chiffre in chiffres:
        entier = int(chiffre)
        cube = entier ** 3
        somme += cube
        print(f"chiffre: {chiffre}, cube: {cube}, somme intermediaire: {somme}")
    return somme

def trouver_nbr():
    resultats = []
    for nbr in range(100, 501):
        if nbr == somme_cube(nbr):
            resultats.append(nbr)
        # else:
        #     print(f"La somme des cubes des chiffres de {nbr} n'est pas égale a lui même.")
    return resultats
    
nombres_trouves = trouver_nbr()
print(f"Les 4 nombres sont:", nombres_trouves)