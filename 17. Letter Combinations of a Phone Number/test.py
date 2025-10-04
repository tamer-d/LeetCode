from letter_combinations import Solution

if __name__ == "__main__":
    digits = input("Entrez les chiffres (2-9) : ")
    result = Solution().letterCombinations(digits)
    print("Toutes les combinaisons possibles :", result)
