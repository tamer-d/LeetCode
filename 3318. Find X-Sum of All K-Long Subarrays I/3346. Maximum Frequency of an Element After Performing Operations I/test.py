from solution import Solution


nums = list(map(int, input("Entrez les nombres (séparés par espaces) : ").split()))
k = int(input("Entrez k : "))
x = int(input("Entrez x : "))

sol = Solution()
res = sol.findXSum(nums, k, x)

print(f"\nInput: nums = {nums}, k = {k}, x = {x}")
print("Output:", res)
