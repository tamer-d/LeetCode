from solution import Solution

if __name__ == "__main__":
    word1 = input("Entrez word1 : ").strip()
    word2 = input("Entrez word2 : ").strip()

    sol = Solution()
    res = sol.validSequence(word1, word2)

    if res:
        print(f"Séquence valide trouvée : {res}")
        print(f"Caractères correspondants : {''.join(word1[i] for i in res)}")
    else:
        print("Aucune séquence valide trouvée.")
