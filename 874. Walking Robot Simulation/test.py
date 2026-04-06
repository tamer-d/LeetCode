from solution import Solution

nums = list(map(int, input("Entrez les nombres triés : ").split()))

sol = Solution()
k = sol.removeDuplicates(nums)

print("\nNombre d’éléments uniques :", k)
print("Tableau après suppression :", nums[:k])
