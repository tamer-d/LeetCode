from solution import Solution

strs = input("Entrez les mots (séparés par des espaces) : ").split()

sol = Solution()
res = sol.longestCommonPrefix(strs)

print(f"\nPréfixe commun le plus long : '{res}'")
