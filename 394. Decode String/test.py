from solution import Solution

s = input("Entrez la chaîne encodée : ")

sol = Solution()
result = sol.decodeString(s)

print(f"\n Chaîne décodée : {result}")
