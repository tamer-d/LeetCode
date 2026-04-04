from solution import Solution

encodedText = input("Entrez le texte encodé : ")
rows = int(input("Entrez le nombre de lignes : "))

sol = Solution()
res = sol.decodeCiphertext(encodedText, rows)

print("\nTexte décodé :")
print(res)
