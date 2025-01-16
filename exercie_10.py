def addition_binaire(A, B):
    # Assurer que les deux nombres ont la même longueur en ajoutant des zéros devant
    max_len = max(len(A), len(B))
    A = A.zfill(max_len)
    B = B.zfill(max_len)
    
    print(f"Nombres alignés :\nA = {A}\nB = {B}")
    
    # Initialisation des variables
    resultat = ""  # Résultat final
    carry = 0  # Retenue (0 ou 1)
    
    # Parcourir les chiffres des deux nombres de droite à gauche
    for i in range(max_len - 1, -1, -1):
        bit_A = int(A[i])  # Convertir le i-ème bit de A en entier
        bit_B = int(B[i])  # Convertir le i-ème bit de B en entier
        
        # Calcul de la somme des bits + retenue
        somme = bit_A + bit_B + carry
        
        # Déterminer le bit du résultat et la nouvelle retenue
        resultat_bit = somme % 2  # 0 ou 1 (résultat de la colonne)
        carry = somme // 2  # 0 ou 1 (retenue pour la prochaine colonne)
        
        # Ajouter le bit au début du résultat
        resultat = str(resultat_bit) + resultat
        
        # Affichage détaillé des étapes
        print(f"Position {i}: bit_A = {bit_A}, bit_B = {bit_B}, carry = {carry}, resultat_bit = {resultat_bit}")
    
    # Ajouter la retenue finale si elle existe
    if carry:
        resultat = "1" + resultat
        print(f"Retenue finale ajoutée : carry = {carry}")
    
    return resultat

A = "1101"
B = "1010"
resultat = addition_binaire(A, B)
print(f"L'addition de {A} et {B} donne : {resultat}")