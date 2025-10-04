#Theo  PIZZARDI M1 CSSD



from sympy import isprime, mod_inverse
from math import gcd


ma_datte_nais = 24111999 #Ma datte de naissance !

#Trouver p blum le plus petit de la datte 

#################EXO 1 RSA signature 

nb_inf = ma_datte_nais # On crée une  nouvelle variable "inférieur" nb_inf a ma datte de naissance ! 
while nb_inf > 2:  # la boucle se stop  avant d’atteindre un nombre inférieur à 2 car le nb blum est un NB P et aucun NB P est inférieur a 2.
    if isprime(nb_inf) and nb_inf % 4 == 3:   #avec isprime verfier si le nb_inf est un NB premier  et si oui il calcule le MODULO est 3  c'est bon 
        p = nb_inf #si le nb_inf est MOD 3 de la multiplication 4 aloes il sotck le nb dans la variable P
        break  #fin de la boucle  while 
    nb_inf -= 1 #et si nb_inf n est pas modulo 3 de la multpl de 4 alors il fait -1 et refait la boucle !!!

#Trouver q blum le plus  grand  de la datte 

nb_sup = ma_datte_nais  # On crée une  nouvelle variable "inférieur"  nb_sup a ma datte de naissance ! 
while True: #Cette boucle while vérifie la condition suivante 
    if isprime(nb_sup) and nb_sup % 4 == 3:  #avec isprime verfier si le nb_sup est un NB premier  et si oui il calcule le MODULO est 3  c'est bon 
        q = nb_sup #si le nb_sup est MOD 3 de la multiplication 4 aloes il sotck le nb dans la variable P
        break
    nb_sup += 1 #et si nb_sup n est pas modulo 3 de la multpl de 4 alors il fait -1 et refait la boucle !!!

print("Nombre premier de Blum inférieur:", p)
print("Nombre premier de Blum supérieur:", q)

n = p * q  # Calcul le n pour faire apres le totient Euler c 'est le module RSA / et pour rabbin 

print("Valeur de n (module RSA):", n) 

TE_n = (p - 1) * (q - 1)  # Calcul du totient Euler et on la met dans la varaible TE_n
print("Valeur de o(n) (Totient d'Euler):", TE_n) 


e = 65537  #  665537C est la norme #cest la clé publique

if gcd(e, TE_n) != 1: # On verifie que e et Tel_n sois premier entre eux qui veux dire que le PGCD doit etre du coup j'ai utiliser la fonction gcd qui calcule le pgcd de e et TEL_n
    raise ValueError("PB les nb ne sont pas premier entre eux change la valeur de  e .")
    
print("e est valider :", e)

d = mod_inverse(e, TE_n)  # on calcule l inverse du MOD de e et Tel_n et mon met ca dans notre varaible 
print("d est valider:", d) #cest la clé privé






key_public = e * n # on crée la clé public
print(key_public)






def texte_en_nombre(texte):
#On convertit le text en en ASCII 

    liste_ascii = [] #On crée une liste 
    for a in texte: # On parcours le texte avec la variable a
        nb_ascii = ord(a)  # avec option ord on converti la a (la lettre a en ASCII) et on stock ASCII dans la varaible nb_ascii
        liste_ascii.append(str(nb_ascii))  # On a joute la variable nb_ascii dans la varaible dans la liste avec apend et j'ai indiquer que cest bien du str pour eviter toute erro 
    print(liste_ascii)
    nombre_texte = ''.join(liste_ascii)  # dans la liste on crée une un text avec join et on la met dans notre nouvelle variable 
    return int(nombre_texte)  # Conversion du txt  en entier avec le int 



def nombre_en_texte(nombre):
    """Convertit un nombre ASCII en texte, caractère par caractère."""
    nombre_str = str(nombre)
    caracteres = []
    i = 0
    while i < len(nombre_str):
        # Essayer de lire un code ASCII sur 3 chiffres (ex: 108, 101 pour 'l', 'e')
        if i + 2 < len(nombre_str) and int(nombre_str[i:i+3]) <= 122:
            code_ascii = int(nombre_str[i:i+3])  # Lire 3 chiffres
            i += 3  # Avancer de 3 positions
        else:
            code_ascii = int(nombre_str[i:i+2])  # Lire 2 chiffres
            i += 2  # Avancer de 2 positions
        
        caracteres.append(chr(code_ascii))  # Convertir en caractère ASCII
    
    return ''.join(caracteres)  # Retourner le texte reconstruit






message = "Theo" 
M = texte_en_nombre(message)  # Conversion en nombre
print("Message converti en nombre est :", M)

signature = pow(M, d, n) #Pow permet de signer mon message qui est stock dans la variable M
#pow fait S=(M**d) mod n #n si non le message est trop grand
#M cest le message en ASCCI 
# d clé privé
#n le module RSA

print("Signature générée:", signature) # le message signer 
print(f' voila quand  on fait l inverse ASCCI en claire  {nombre_en_texte(84104101111)}')


# ---------------------------- Étape 5 : Vérification de la signature ---------------------------- #



M_verifie = pow(signature, e, n)  # Vérification avec key_public
# on calcule la signature dans le message 
#e c est la cle publique
print("Message après vérification:", M_verifie)


if M_verifie == M: # 
    print(" le message est authentique.")
else:
    print(" le message a été modifié.")



#######################EXO PARTI 1 

C = pow(M, 2, n)  #M puissance 2  MOD n pow permet de calculer la puissance 
print("Message chiffré (C = M^2 mod n) est :", C)


def rabin_dechiffre(C, p, q, n): #on recupere C message chiffrer ; p et q trouver la racine de p et q et on a beson de n qui est le n = q * p po
    # a) Racines modulo p et q pour trouver x**2 = k * n + c
    Mp = pow(C, (p + 1)//4, p) # Calcule la racine carrée de C modulo p
    Mq = pow(C, (q + 1)//4, q)

  
    racines_p = [Mp, p - Mp]   #stocke les 2 solutions la racine C de p et q 
    racines_q = [Mq, q - Mq] 

    solutions = [] 

    for rp in racines_p:
        for rq in racines_q: # Pour chaque couple on cal la solution de x MOD n pour trouver le reste chinois 
           
            inv_p = mod_inverse(p, q) 
            inv_q = mod_inverse(q, p)

            x = (rp * q * inv_q + rq * p * inv_p) % n # on applique les nouvelle racine dans le théoreme chinois 
            solutions.append(x)

    for sol in solutions:
        if sol == M:  # On compare directement au nombre M
            return sol  # On renvoie la bonne solution

    return None  # Si on ne la trouve pas

resultat = rabin_dechiffre(C, p, q, n)

if resultat == M_verifie: #petite condition pour bien verfier !
    print(f"Le message a bien été déchiffrer : message OG {M_verifie} et  le message Dechiffrer  {resultat}")



#################################EXO 2 PAT 2 et 3 

Mp = pow(C, (p + 1)//4, p)   # sqrt(C) mod p (p ≡ 3 mod 4)
Mq = pow(C, (q + 1)//4, q)   # sqrt(C) mod q (q ≡ 3 mod 4)

racines_p = [Mp, p - Mp]     # x et -x modulo p
racines_q = [Mq, q - Mq]     # x et -x modulo q

solutions = []
inv_p = mod_inverse(p, q)    # p⁻¹ mod q pour CRT
inv_q = mod_inverse(q, p)    # q⁻¹ mod p pour CRT

for rp in racines_p:         # Combine racines part. p
    for rq in racines_q:     # et racines part. q
        x = (rp * q * inv_q + rq * p * inv_p) % n  # CRT
        solutions.append(x)

solutions = sorted(set(solutions))  # Enlève doublons
print("\n(2) Les 4 solutions x où x^2 = C mod n :", solutions)

x, y = None, None
for i in range(len(solutions)):     # On parcourt x,y
    for j in range(i+1, len(solutions)):
        a, b = solutions[i], solutions[j]
        if a != b and a != (n - b) % n:  # x ≠ ±y
            x, y = a, b
            break
    if x is not None:
        break

if x is None:
    print("Aucun x,y non trivial trouvé.")
else:
    print(f"\n(2) x={x}, y={y}, x^2≡y^2 mod n, x≠±y.")
    d = gcd(x + y, n)               # gcd(x+y,n)
    print(f"(3) gcd(x+y, n) = {d}")
    if 1 < d < n:
        print(f"Facteurs : p={d}, q={n//d}")
    else:
        print("PGCD trivial, pas de factorisation.")




###EXO 3 BBS

x = 24111999  # Graine : ma date de naissance
bits = []     # Liste pour stocker les bits

for i in range(128):      # je veux  128 bits
    x = pow(x, 2, n)      # je change  x par x^2 mod n
    bit = x & 1           # je récupere le bit de poids faible (LSB) 
                          # & 1 : c'est le masque binaire pour extraire le dernier bit
    bits.append(str(bit)) # je rajoute  bit (sous forme texte) à la liste

sequence_128_bits = ''.join(bits)  # j'ai  assemblé les bits en une chaîne 1 a 1 plus simple a comprendre 

print("Séquence BBS (128 bits) =", sequence_128_bits)





