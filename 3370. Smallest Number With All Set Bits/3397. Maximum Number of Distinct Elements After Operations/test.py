from solution import Solution

n = int(input("Entrez un entier n : "))

sol = Solution()
ans = sol.smallestNumber(n)

print(f"Input: n = {n}")
print(f"Output: {ans}")
print(f"Binary form: {bin(ans)[2:]}")
