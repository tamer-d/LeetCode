from solution import Solution

if __name__ == "__main__":

    word1 = input("Entrez le premier mot : ").strip()
    word2 = input("Entrez le deuxième mot : ").strip()

    sol = Solution()
    result = sol.minDistance(word1, word2)

    print(f"\nNombre minimum de suppressions nécessaires : {result}")
