from solution import Solution

heights = list(map(int, input("Entrez les hauteurs (séparées par des espaces) : ").split()))

sol = Solution()
result = sol.heightChecker(heights)

print(f"\nNombre d'élèves mal placés : {result}")
