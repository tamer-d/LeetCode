from solution import Solution

nums = list(map(int, input("Entrez les nombres (séparés par des espaces) : ").split()))

sol = Solution()
result = sol.majorityElement(nums)

print(f"\nÉlément majoritaire : {result}")
