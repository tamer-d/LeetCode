from solution import Solution

n = int(input("Entrez le numéro de colonne Excel : "))

sol = Solution()
result = sol.convertToTitle(n)

print(f"\n Titre de la colonne Excel : {result}")
