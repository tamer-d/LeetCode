from solution import Solution

nums = list(map(int, input("Entrez les éléments du tableau (séparés par des espaces) : ").split()))

sol = Solution()
res = sol.longestBalanced(nums)

print(f"\nInput: {nums}")
print(f"Output (longueur maximale balanced) : {res}")
