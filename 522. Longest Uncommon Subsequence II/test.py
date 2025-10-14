from solution import Solution

if __name__ == "__main__":
    strs = input("Entrez la liste de mots séparés par des espaces : ").split()

    sol = Solution()
    result = sol.findLUSlength(strs)
    print("\n Longest Uncommon Subsequence Length :", result)
