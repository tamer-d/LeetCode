from solution import Solution

if __name__ == "__main__":

    nums = list(map(int, input("Entrez les éléments de nums séparés par des espaces : ").split()))
    k = int(input("Entrez la valeur de k : "))
    numOperations = int(input("Entrez la valeur de numOperations : "))

    sol = Solution()
    result = sol.maxFrequency(nums, k, numOperations)
    print(f"\n Fréquence maximale possible : {result}")
