from solution import Solution

if __name__ == "__main__":
    deck = list(map(int, input("Entrez les cartes séparées par des espaces : ").split()))
    sol = Solution()
    possible, groups = sol.hasGroupsSizeX(deck)

    print("\nRésultat :", possible)
    if possible:
        print("TRUE :\nGroupes formés :")
        for g in groups:
            print(g)
    else:
        print("FAUX : Aucun groupement possible.")
