# Fonction récursive pour calculer l'ANF (Forme Algébrique Normale)
def calculer_anf(table, debut, taille):
    # Cas de base : un seul élément, on ne fait rien
    if taille <= 1:
        return

    moitié = taille // 2

    # Traitement récursif sur la première moitié
    calculer_anf(table, debut, moitié)

    # Traitement récursif sur la deuxième moitié
    calculer_anf(table, debut + moitié, moitié)

    # Combinaison des deux moitiés avec XOR
    for i in range(moitié):
        table[debut + moitié + i] ^= table[debut + i]


# Fonction pour afficher l'ANF sous forme lisible
def afficher_anf(n, table):
    taille = 1 << n  # 2 puissance n
    premier = True  # pour éviter le + au début

    for masque in range(taille):
        if table[masque] == 1:
            if not premier:
                print(" + ", end="")
            premier = False

            if masque == 0:
                print("1", end="")  # Terme constant
            else:
                for i in range(n):
                    if masque & (1 << i):
                        print(f"x{i+1}", end="")
    if premier:
        print("0", end="")  # si aucun terme n’a été affiché
    print()  # saut de ligne final


# Programme principal
def main():
    n = 3  # nombre de variables (par exemple : x1, x2, x3)
    taille = 1 << n  # taille de la table = 2^n
    table_verite = [0, 1, 1, 0, 0, 1, 0, 1]  # table de vérité donnée
    anf = table_verite.copy()  # copie de travail

    # Calcul de l'ANF avec la méthode récursive
    calculer_anf(anf, 0, taille)

    # Affichage du résultat
    print("Forme Algébrique Normale (méthode divisée) : ", end="")
    afficher_anf(n, anf)


# Exécuter le programme
main()


