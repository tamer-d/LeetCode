from solution import Solution

s = input("Entrez la chaîne initiale : ")
a = int(input("Entrez la valeur de a : "))
b = int(input("Entrez la valeur de b : "))

sol = Solution()
res = sol.findLexSmallestString(s, a, b)
print(f"\n La plus petite chaîne lexicographique possible est : {res}")
