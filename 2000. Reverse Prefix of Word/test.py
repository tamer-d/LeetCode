from reverse_prefix import Solution

if __name__ == "__main__":
    word = input("Entrez le mot : ")
    ch = input("Entrez le caractère : ")
    sol = Solution()
    print("Résultat :", sol.reversePrefix(word, ch))
