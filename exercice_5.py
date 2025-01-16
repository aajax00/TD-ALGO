def convert_binaire(nbr):
    if nbr < 0:
        return "Le nombre doit etre += 0"
    if nbr == 0:
        return "0"
        
    binaire = ""
    while nbr > 0:
        reste = nbr % 2
        binaire = str(reste) + binaire
        nbr = nbr // 2
    return binaire
    
nbr = 1998
binaire = convert_binaire(nbr)
print(f"La representation binaire de {nbr} est: {binaire}")