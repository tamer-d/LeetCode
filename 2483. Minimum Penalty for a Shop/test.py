from solution import Solution

customers = input("Entrez la chaîne (Y/N) : ").strip()

sol = Solution()
res = sol.bestClosingTime(customers)

print(f"\nMeilleure heure de fermeture : {res}")
