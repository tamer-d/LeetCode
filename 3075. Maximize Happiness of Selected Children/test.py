from solution import Solution

def main():
    happiness = list(map(int, input("Entrez la liste des bonheurs (séparés par des espaces) : ").split()))
    k = int(input("Entrez le nombre d'enfants à sélectionner (k) : "))

    sol = Solution()

    result = sol.maximumHappinessSum(happiness, k)
    print("Bonheur maximal obtenu :", result)

if __name__ == "__main__":
    main()
