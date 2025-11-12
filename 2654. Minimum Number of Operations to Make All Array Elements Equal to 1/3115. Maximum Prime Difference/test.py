from solution import Solution

nums = list(map(int, input("Entrez la liste d'entiers (séparés par espace) : ").split()))
sol = Solution()
res = sol.minOperations(nums)

print(f"\nRésultat : {res}")
