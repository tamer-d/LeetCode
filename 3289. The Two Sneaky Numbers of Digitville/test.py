from solution import Solution

nums = list(map(int, input("Entrez les nombres (séparés par des espaces) : ").split()))

sol = Solution()
res = sol.getSneakyNumbers(nums)

print(f"\nInput: nums = {nums}")
print(f"Output: {res}")
