from solution import Solution

if __name__ == "__main__":
    print("Entrez les matchs (winner loser), séparés par des virgules :")
    raw = input("Exemple: 1 3, 2 3, 3 6 : ")
    matches = [list(map(int, pair.strip().split())) for pair in raw.split(',')]

    sol = Solution()
    res = sol.findWinners(matches)

    print("\nJoueurs sans défaite  :", res[0])
    print("Joueurs avec une défaite :", res[1])
