from solution import Solution

if __name__ == "__main__":
    nums = list(map(int, input("Entrez les éléments de nums séparés par espaces : ").split()))
    k = int(input("Entrez la valeur de k : "))

    sol = Solution()
    result = sol.maxDistinctElements(nums, k)
    print(f"\n Nombre maximal d’éléments distincts possible : {result}")
