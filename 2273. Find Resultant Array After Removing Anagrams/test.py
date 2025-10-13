from solution import Solution

if __name__ == "__main__":
    sol = Solution()

    user_input = input("Entrez les mots séparés par des espaces : ")
    words = user_input.strip().split()

    result = sol.removeAnagrams(words)

    print("Liste avant suppression des anagrammes :", words)
    print("Liste après suppression des anagrammes :", result)