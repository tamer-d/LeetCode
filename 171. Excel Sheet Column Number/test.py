from solution import Solution

title = input("Entrez le titre de colonne Excel (ex: AB) : ").strip().upper()

sol = Solution()
result = sol.titleToNumber(title)

print(f"\nNuméro correspondant : {result}")
