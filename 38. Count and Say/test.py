from solution import Solution

n = int(input("Entrez la valeur de n : "))

sol = Solution()
res = sol.countAndSay(n)

print(f"\nRésultat pour n = {n} :")
print(res)
