def fibonacci(n):
    if n <= 0:
        return "N doit etre un entier"
    elif n == 1 or n == 2:
        return 1
    else:
        U0, U1 = 1, 1
        for i in range(2, n):
            Un = U0 + U1
            U0, U1 = U1, Un
        return Un
        
N = 6
resultat = fibonacci(N)
print(f"le {N}ème terme de la suite de FIBONACCI est: {resultat}")