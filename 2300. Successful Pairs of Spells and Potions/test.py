from successful_pairs import Solution

if __name__ == "__main__":
    print("=== Successful Pairs of Spells and Potions ===")

    spells = list(map(int, input("Entrez les puissances des sorts (ex: 5 1 3) : ").split()))
    potions = list(map(int, input("Entrez les puissances des potions (ex: 1 2 3 4 5) : ").split()))
    success = int(input("Entrez la valeur de succès minimale : "))

    sol = Solution()
    result = sol.successfulPairs(spells, potions, success)

    print("\nRésultat :", result)
