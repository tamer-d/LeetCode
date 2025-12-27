from solution import Solution

candidates = list(map(int, input("Entrez les nombres (séparés par espace) : ").split()))
target = int(input("Entrez la valeur target : "))

sol = Solution()
res = sol.combinationSum2(candidates, target)

print("\nCombinaisons possibles :")
for comb in res:
    print(comb)
