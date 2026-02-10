from solution import Solution

s = input("Entrez la chaîne de chiffres : ").strip()

sol = Solution()
res = sol.areDigitsEqual(s)

print(f"\nRésultat : {res}")
