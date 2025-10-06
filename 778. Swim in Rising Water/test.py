from swim_in_rising_water import Solution

if __name__ == "__main__":
    n = int(input("Entrez la dimension n de la grille : "))
    print("Entrez les lignes de la grille, chaque ligne sur une nouvelle ligne, éléments séparés par espace :")
    grid = []
    for _ in range(n):
        row = list(map(int, input().split()))
        grid.append(row)

    result = Solution().swimInWater(grid)
    print("Temps minimum pour atteindre la destination :", result)
