from solution import Solution

nums = list(map(int, input("Entrez les scores (séparés par des espaces) : ").split()))
k = int(input("Entrez la valeur de k : "))

sol = Solution()
result = sol.minimumDifference(nums, k)

print(f"Différence minimale = {result}")
