from solution import Solution

nums = list(map(int, input("Entrez les nombres (séparés par des espaces) : ").split()))

sol = Solution()
res = sol.nextGreaterElements(nums)

print(f"\nInput: {nums}")
print(f"Output: {res}")
