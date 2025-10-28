from solution import Solution

nums = list(map(int, input("Entrez les éléments du tableau (séparés par des espaces) : ").split()))

sol = Solution()
result, steps = sol.minimumOperations(nums)

print(f"\nInput: nums = {nums}")
print(f"nombre de steps: {result}\n")
print("étapes :")
for m, arr in steps:
    print(f"- Soustraire {m} → {arr}")
